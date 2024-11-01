from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

list = soup.find_all(name="h3", class_="title")
print(list)
greatest_movies = [movie.getText() for movie in list]

with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movie in greatest_movies:
        movie_name = f"{movie}\n"
        file.write(movie_name)

print(greatest_movies)


