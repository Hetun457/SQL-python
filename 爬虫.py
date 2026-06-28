from mysqlHelper import MySqlHelper
import requests
import json
import re

db = MySqlHelper(
    host="localhost",
    user="root",
    password="",
    database="studenttable" 
)

def get_baidu_hot():

    url = "https://top.baidu.com/board?tab=realtime"

    headers = {
        "User-Agent":"Mozilla/5.0"
    }

    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    html = resp.text

    result = re.search(r'<!--s-data:(.*?)-->', html, re.S)

    if result is None:
        print("没有找到数据")
        return []

    json_text = result.group(1)

    data = json.loads(json_text)

    hot_list = data["data"]["cards"][0]["content"]

    data_list = []

    for item in hot_list[:10]:

        rank = item["index"]
        title = item["word"]

        try:
            hot = int(item["hotScore"])
        except:
            hot = 0

        data_list.append([rank, title, hot])

    return data_list


if __name__ == "__main__":

    hot_data = get_baidu_hot()

    insert_sql = """
    INSERT INTO baidu_hot(hot_rank, title, hot_value)
    VALUES (%s, %s, %s)
    """

    for item in hot_data:
        db.execute(insert_sql, item)
        print(f"成功存入：第{item[0]}名 {item[1]}")

    db.close()

    print("successful saved")
