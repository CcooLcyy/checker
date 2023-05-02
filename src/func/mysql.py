import pymysql, zipfile, hashlib
from file import File

class Mysql():
    def __init__(self):
        self.file = File()
        try:
            self.connection = pymysql.connect(
                host = 'localhost',
                user = 'checker',
                password = 'password',
                database = 'checker'
            )
            self.installed = True
            if self.connection != None:
                self.cursor = self.connection.cursor()
            self.verifyPassword('admin')
        except TypeError:
                self.__insert('user', user_id = 1, user_name = 'admin', user_password = 'admin')
        except Exception as e:
            if e.args[0] == 2003:
                self.installed = False

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def __installMysql(self):
        installPath = self.file.selectDirPath()
        zipPath = 'res/mysql-5.7.41-winx64.zip'
        with zipfile.ZipFile(zipPath, 'r') as zip_ref:
            zip_ref.extractall(installPath)

    def __insert(self, tableName, **kwargs):
        columns = ', '.join(kwargs.keys())
        placeholders = ', '.join(['%s'] * len(kwargs))
        values = tuple(kwargs.values())
        insert = f"INSERT INTO {tableName} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert, values)
        self.connection.commit()

    def __query(self, tableName, *args, **kwargs):
        columns = ', '.join(args)
        if len(kwargs) != 0:
            condition = 'AND'.join(f"{key}='{value}'"for key, value in kwargs.items())
            query = f"SELECT {columns} FROM {tableName} WHERE {condition}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        else:
            # condition = 'AND'.join(f"{key}='{value}'"for key, value in kwargs.items())
            query = f"SELECT {columns} FROM {tableName}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

    def md5_encrypt(self, text):
        msg = hashlib.md5()
        msg.update(text.encode('utf-8'))
        return msg.hexdigest()

    def verifyPassword(self, userName):
        test = f"user_name = '{userName}'"
        self.cursor.execute(f"SELECT user_password FROM user WHERE {test}")
        result = self.cursor.fetchone()
        return result[0]
    
    def addUser(self, userName, password):
        passwordMd5 = self.md5_encrypt(password)
        self.__insert('user', user_name = userName, user_password = passwordMd5)
        self.connection.commit()
    
    def test(self):
        result = self.__query('user', '*')
        print(result)

if __name__ == "__main__":
    sql = Mysql()
    sql.test()