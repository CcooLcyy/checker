import pymysql

class Mysql():
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'checker',
            password = '....',
            database = 'checker'
        )
        self.cursor = self.connection.cursor()
        print('1')

    def __del__(self):
        self.cursor.close()
        self.connection.close()

def main():
    sql = Mysql()

if __name__ == "__main__":
    main()