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
            if not self.userExist('admin'):
                self.__insert('user', {'user_id': '1', 'user_name': 'admin', 'user_password': f"{self.md5_encrypt('admin')}"})
                self.__init__()
        except Exception as e:
            if e.args[0] == 2003:
                self.installed = False
            elif e.args[0] == 1146:
                self.__createTable('user', {'user_id': 'INT(32) AUTO_INCREMENT PRIMARY KEY', 'user_name': 'CHAR(32)', 'user_password': 'CHAR(32)'})
            self.__init__()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    # def installMysql(self):
    #     installPath = self.file.selectDirPath()
    #     zipPath = 'res/mysql-5.7.41-winx64.zip'
    #     with zipfile.ZipFile(zipPath, 'r') as zip_ref:
    #         zip_ref.extractall(installPath)

    def __insert(self, tableName, row):
        columns = ', '.join(row.keys())
        placeholders = ', '.join(['%s'] * len(row))
        values = tuple(row.values())
        insert = f"INSERT INTO {tableName} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert, values)
        self.connection.commit()

    def __query(self, table_name, *column_names, conditions=None):
        columns_str = ', '.join(column_names)
        if conditions:
            conditions_str = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            sql = f"SELECT {columns_str} FROM {table_name} WHERE {conditions_str}"
            values = tuple(conditions.values())
            self.cursor.execute(sql, values)
        else:
            sql = f"SELECT {columns_str} FROM {table_name}"
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __createTable(self, table_name, columns):
        columns_str = ', '.join([f"{column_name} {column_type}" for column_name, column_type in columns.items()])
        sql = f"CREATE TABLE {table_name} ({columns_str})"
        self.cursor.execute(sql)
        self.connection.commit()
    
    def __update(self, table_name, data, condition):
        set_values = ', '.join([f"{key} = %s" for key in data.keys()])
        condition_str = ' AND '.join([f"{key} = %s" for key in condition.keys()])
        sql = f"UPDATE {table_name} SET {set_values} WHERE {condition_str}"
        values = list(data.values()) + list(condition.values())
        self.cursor.execute(sql, values)
        self.connection.commit()

    def md5_encrypt(self, text):
        msg = hashlib.md5()
        msg.update(text.encode('utf-8'))
        return msg.hexdigest()

    def userExist(self, userName):
        result = self.__query('user', 'user_name', conditions={'user_name': f'{userName}'})
        if len(result) == 0:
            return False
        elif result[0][0] == userName:
            return True
        
    def verifyPassword(self, userName):
        result = self.__query('user', 'user_password', conditions={'user_name': f'{userName}'})
        print(result[0][0])

    def addUser(self, userName, password):
        if self.__query('user', {'user_name': f'{userName}', 'user_password': f'{self.md5_encrypt(f"{password}")}'}):
            print('用户存在')
        else:
            passwordMd5 = self.md5_encrypt(password)
            self.__insert('user', {'user_name': f'{userName}', 'user_password': f'{passwordMd5}'})
            self.connection.commit()
        
    def password(self, userName, password):
        passwordMd5 = self.md5_encrypt(password)
        self.__update('user', {'user_password': f'{passwordMd5}'}, {'user_name':f'{userName}'})
    
    def test(self):
        pass

if __name__ == "__main__":
    sql = Mysql()