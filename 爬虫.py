from mysqlHelper import MySqlHelper
import requests
import json
import re

class BaiduSpider:

    def __init__(self):
        self.db =  MySqlHelper(
            host="localhost",
            user="root",
            password="",
            database="studenttable" 
        )
        
        self.url = "https://top.baidu.com/board?tab=realtime"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        
    def get_baidu_hot(self):
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

def save_data(self, hot_data):

        insert_sql = """
        INSERT INTO baidu_hot(hot_rank, title, hot_value)
        VALUES (%s, %s, %s)
        """

        for item in hot_data:
            self.db.execute(insert_sql, item)
            print(f"成功存入：第{item[0]}名 {item[1]}")
            
 def run(self):
        hot_data = self.get_baidu_hot()

        if hot_data:
            self.save_data(hot_data)
        self.db.close()
        print("successful saved")

if __name__ == "__main__":
    spider = BaiduSpider()
    spider.run()

   
