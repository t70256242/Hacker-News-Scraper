
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class Scraper:
    def __init__(self):
        self.URL = "https://news.ycombinator.com/news"

    def scrape_data(self):
        try:
            response = requests.get(self.URL, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            print("The request timed out. Retrying...")
            time.sleep(5)
            return self.scrape_data()
        except requests.exceptions.ConnectionError:
            print("Failed to connect to the server. Retrying...")
            time.sleep(10)
            return self.scrape_data()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred during the request: {req_err}")
            return None

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            table_ = soup.select_one("#hnmain")
            if table_ is None:
                raise ValueError("Unable to find the main content table on the page.")

            list_ = table_.find_all("tr")

            topic = []
            href = []
            upvote = []
            user = []
            comments = []

            for a in table_.select("td .title a"):
                if 'from?site=' in a.get('href') or 'item?id=41291219' in a.get('href') or '?p=2' in a.get('href'):
                    continue
                else:
                    topic.append(a.text.strip())
                    href.append(a.get('href'))

            for td in table_.select("tr .subtext"):
                if 'points' not in td.text.strip():
                    upvote.append(0)
                    user.append('nan')
                    comments.append('nan')
                else:
                    try:
                        upvote.append(td.text.strip().split('by')[0].split(' points')[0])
                    except:
                        upvote.append(0)
                    try:
                        user.append(td.text.strip().split('by')[1].split(' ')[1].strip())
                    except:
                        user.append('nan')
                    try:
                        comments.append(td.text.strip().split('by')[1].split('| hide |')[1].strip().split('comments')[0])
                    except:
                        comments.append('nan')

            data = pd.DataFrame(
                {'topic': topic, 'href': href, 'upvote': upvote, 'user': user, 'comments': comments}
            ).sort_values(by=['upvote', 'comments'], ascending=False, ignore_index=True)

            data['upvote'] = pd.to_numeric(data['upvote'])
            data['comments'] = data['comments'].apply(lambda x: x.translate({ord('\xa0'): None}))
            data['comments'] = data['comments'].apply(lambda x: x if isinstance(x, str) and x.isdigit() else 0)
            data['comments'] = pd.to_numeric(data['comments'])
            data.sort_values(by=['upvote', 'comments'], ascending=False, inplace=True)
            data.reset_index(drop=True, inplace=True)

            return data

        except ValueError as ve:
            print(f"Value error: {ve}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
