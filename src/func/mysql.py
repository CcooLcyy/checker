import pymysql

class Mysql():
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host = 'localhost',
                user = 'checker',
                password = 'password',
                database = 'checker'
            )
            self.installed = True
        except Exception as e:
            if e.args[0] == 2003:
                self.installed = False

    def __del__(self):
        # self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    sql = Mysql()