from bs4 import BeautifulSoup


with open("website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.li)
print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

#Getting values from CSS selector
name = soup.select_one(selector="#name") #Getting the first element that has id name
print(name)

heading = soup.select(".heading") #Getting all elements who has class heading
print(heading)
