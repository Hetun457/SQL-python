from mysqlHelper import MySqlHelper
import requests
from bs4 import BeautifulSoup
import re

db = MySqlHelper(
    host="localhost",
    user="root",
    password="1388@jiaM",
    database="movie_db"
)


def get_movie():

    headers = {"User-Agent": "Mozilla/5.0"}

    data_list = []

    for start in range(0, 100, 25):

        url = f"https://movie.douban.com/top250?start={start}"

        resp = requests.get(url, headers=headers)
        resp.encoding = "utf-8"

        soup = BeautifulSoup(resp.text, "html.parser")

        movies = soup.find_all("div", class_="item")

        for movie in movies:
            ranking = int(movie.find("em").text)
            movie_name = movie.find("span", class_="title").text
            score = float(movie.find("span", class_="rating_num").text)
            rating_div = movie.find("span", class_="rating_num").parent
            star_text = rating_div.get_text(" ", strip=True)

            result = re.search(r'(\d+)人评价', star_text)

            if result:
                comment_count = int(result.group(1))
            else:
                comment_count = 0
            p = movie.find("p")

            if p:
                info = p.get_text(" ", strip=True)
            else:
                info = ""

            year_result = re.search(r'(\d{4})', info)

            if year_result:
                year = int(year_result.group(1))
            else:
                year = 0

            country = ""
            movie_type = ""

            if year_result:
                temp = info.split(year_result.group(1))

                if len(temp) > 1:
                    detail = temp[1].replace("/", " ").split()

                    if len(detail) >= 1:
                        country = detail[0]

                    if len(detail) >= 2:
                        movie_type = " ".join(detail[1:])

            director = ""

            director_result = re.search(r'导演:\s*(.*?)\s*主演:', info)

            if director_result:
                director = director_result.group(1)

            actor = ""

            actor_result = re.search(r'主演:\s*(.*?)\s*\d{4}', info)

            if actor_result:
                actor = actor_result.group(1)

            quote = movie.find("span", class_="inq")

            if quote:
                quote = quote.text
            else:
                quote = ""

            data_list.append([
                ranking,
                movie_name,
                score,
                comment_count,
                director,
                actor,
                year,
                country,
                movie_type,
                quote
            ])

    return data_list


if __name__ == "__main__":

    movie_data = get_movie()

    insert_sql = """
    INSERT INTO movie
    (ranking, movie_name, score, comment_count,
    director, actor, year, country, movie_type, quote)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for item in movie_data:
        db.execute(insert_sql, item)
        print(f"成功存入：第{item[0]}名 {item[1]}")

    db.close()

    print("successful saved")
