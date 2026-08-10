from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)

CORS(app)

@app.route("/sales")
def get_sales():
    
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1388@jiaM",
        database="chart_db"
    )
    
    cursor = conn.cursor()
    sql = "SELECT name, count FROM sales"
    cursor.execute(sql)
    result = cursor.fetchall()

    data = []

    for row in result:

        data.append({
            "name": row[0],
            "count": row[1]
        })


    cursor.close()
    conn.close()
    
    return jsonify(data)


if __name__ == "__main__":

    app.run(port=5000)
