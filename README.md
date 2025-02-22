# 📰 Hacker News Scraper

A simple Python script to scrape top news articles from [Hacker News](https://news.ycombinator.com/) using **Requests** and **BeautifulSoup**.

## 🚀 Features
- Extracts article titles and links.
- Retrieves upvotes, usernames, and comment counts.
- Handles errors like timeouts, connection issues, and missing data.
- Returns data as a structured **Pandas DataFrame**.
- Sorts articles based on upvotes and comment count.

## 🛠️ Tech Stack
- **Python**
- **Requests** (for fetching web pages)
- **BeautifulSoup** (for parsing HTML)
- **Pandas** (for data handling)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/HackerNews-Scraper.git
   cd HackerNews-Scraper
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Usage

Run the script to scrape Hacker News articles:
```python
from scraper import Scraper

scraper = Scraper()
data = scraper.scrape_data()
print(data)
```

## 🖼️ Example Output
```
                           topic                                              href  upvote      user comments
0  Exciting New Tech Trends     https://news.ycombinator.com/item?id=12345     150   johndoe       42
1      AI in Healthcare       https://example.com/ai-healthcare                 95   janedoe       30
...
```

[Visit PrOrganize Manager]([http://ec2-13-51-162-119.eu-north-1.compute.amazonaws.com/](https://my-portfolio-website-sxuy.onrender.com/blog))


## 👥 Contributing
Contributions are welcome! Feel free to submit a **pull request** or open an **issue**.

## 📄 License
This project is licensed under the **MIT License**.

## 🔗 Links
- **Project Repository**: [GitHub](https://github.com/yourusername/HackerNews-Scraper)
- **Hacker News**: [https://news.ycombinator.com/](https://news.ycombinator.com/)

