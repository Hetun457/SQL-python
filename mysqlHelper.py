import pymysql

class MySqlHelper:

    def __init__(self, host="localhost", port=3306, user="root",
                 password="", database="test_db"):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = database

        self.conn = None
        self.cursor = None

    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db,
                charset="utf8mb4"
            )
            self.cursor = self.conn.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

        self.cursor = None
        self.conn = None

    def execute(self, sql, params=()):
        try:
            self.get_conn()
            self.cursor.execute(sql, params)
            self.conn.commit()
            return self.cursor.rowcount

        except Exception as e:
            if self.conn:
                self.conn.rollback()
            print("wrong statement:", e)
            return 0

        finally:
            self.close()

    def get_one(self, sql, params=()):
        try:
            self.get_conn()
            self.cursor.execute(sql, params)
            return self.cursor.fetchone()

        except Exception as e:
            print("wrong query:", e)
            return None

        finally:
            self.close()

    def get_all(self, sql, params=()):
        try:
            self.get_conn()
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()

        except Exception as e:
            print("wrong queries:", e)
            return []

        finally:
            self.close()


if __name__ == "__main__":
    db = MySqlHelper(password="")
    res = db.get_all("select * from student")
    print(res)

