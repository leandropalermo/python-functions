from bs4 import BeautifulSoup, Tag
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(".titleline > a")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.get_text()
    article_link = article_tag.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [ int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_upvote = max(article_upvotes)
index = article_upvotes.index(max_upvote)

print(article_links[index])
print(article_texts[index])
