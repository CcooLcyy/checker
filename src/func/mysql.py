import pymysql, zipfile, hashlib
from .file import File

class Mysql():
    def __init__(self):
        self.file = File()
        self.user_table = 'users'
        self.prod_table = 'products'
        self.mat_table = 'materials'
        self.bom_table = 'boms'
        self.mark_table = 'marks'
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
                self.__insert(self.user_table, {'user_id': '1', 'user_name': 'admin', 'user_password': f"{self.md5_encrypt('admin')}"})
                self.__init__()
        except Exception as e:
            if e.args[0] == 2003:
                self.installed = False
            elif e.args[0] == 1146:
                self.__createTable(self.user_table, {'user_id': 'INT(32) AUTO_INCREMENT PRIMARY KEY', 'user_name': 'CHAR(32)', 'user_password': 'CHAR(32)'})
                self.__createTable(self.prod_table, {'prod_id': 'INT(32) PRIMARY KEY', 'prod_name': 'CHAR(32)'})
                self.__createTable(self.mat_table, {'mat_id': 'INT(32) PRIMARY KEY', 'mat_name': 'CHAR(32)'})
                self.__createTable(self.bom_table, {'prod_id': 'INT(32)', 'mat_id': 'INT(32)'})
                self.__createTable(self.mark_table, {'classed_id': 'INT(32) AUTO_INCREMENT PRIMARY KEY' , 'mat_id': 'INT(32)', 'prod_id': 'INT(32)', 'user_id': 'INT(32)', 'mark_time': 'DATETIME', 'a_class': 'BOOL', 'b_class': 'BOOL', 'c_class': 'BOOL'})
            elif e.args[0] == 1049:
                self.connection = pymysql.connect(
                    host='localhost',
                    user='checker',
                    password='password',
                )
                self.cursor = self.connection.cursor()
                self.cursor.execute('CREATE DATABASE checker;')
                self.connection.commit()
            else:
                print(e)
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

    def __query(self, tableName, conditions=None, *column_names):
        columnsStr = ', '.join(column_names)
        if conditions:
            conditionsStr = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            sql = f"SELECT {columnsStr} FROM {tableName} WHERE {conditionsStr}"
            values = tuple(conditions.values())
            self.cursor.execute(sql, values)
        else:
            sql = f"SELECT {columnsStr} FROM {tableName}"
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def __subQuery(self, tableName, subTableName, conditions=None, subConditions=None, *subColumnNames):
        subQueryResult = ', '.join([str(x[0]) for x in self.__query(subTableName, subConditions, *subColumnNames)])
        if conditions:
            conditionsStr = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
            sql = f"SELECT * FROM {tableName} WHERE {conditionsStr} AND {subColumnNames[0]} IN ({subQueryResult})"
            values = tuple(conditions.values())
            self.cursor.execute(sql, values)
        else:
            sql = f"SELECT * FROM {tableName} WHERE {subColumnNames[0]} IN ({subQueryResult})"
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __createTable(self, tableName, columns):
        columnsStr = ', '.join([f"{columnName} {columnType}" for columnName, columnType in columns.items()])
        sql = f"CREATE TABLE {tableName} ({columnsStr})"
        self.cursor.execute(sql)
        self.connection.commit()
    
    def __update(self, tableName, data, condition):
        setValues = ', '.join([f"{key} = %s" for key in data.keys()])
        conditionStr = ' AND '.join([f"{key} = %s" for key in condition.keys()])
        sql = f"UPDATE {tableName} SET {setValues} WHERE {conditionStr}"
        values = list(data.values()) + list(condition.values())
        self.cursor.execute(sql, values)
        self.connection.commit()

    def __delete(self, tableName: str, condition: map) -> None:
        conditionStr = ' AND '.join([f"{key} = %s" for key in condition.keys()])
        sql = f"DELETE FROM {tableName} WHERE {conditionStr}"
        value = tuple(condition.values())
        self.cursor.execute(sql, value)
        self.connection.commit()

    def md5_encrypt(self, text: str) -> str:
        msg = hashlib.md5()
        msg.update(text.encode('utf-8'))
        return msg.hexdigest()

    def userExist(self, userName: str):
        result = self.__query(self.user_table, {'user_name': f'{userName}'}, 'user_name')
        if len(result) == 0:
            return False
        elif result[0][0] == userName:
            return True
        
    def verifyPassword(self, userName):
        result = self.__query(self.user_table, {'user_name': f'{userName}'}, 'user_password')
        if len(result) != 0:
            return result[0][0]

    def addUser(self, userName, password):
        passwordMd5 = self.md5_encrypt(password)
        if self.__query(self.user_table, {'user_name': f'{userName}', 'user_password': f'{passwordMd5}'}, 'user_name'):
            return '用户存在'
        else:
            self.__insert(self.user_table, {'user_name': f'{userName}', 'user_password': f'{passwordMd5}'})
            return f'用户：{userName}添加成功，密码为：{password}'
        
    def changePassword(self, userName, password):
        if not self.userExist(userName):
            return '用户不存在，请先添加用户'
        else:
            passwordMd5 = self.md5_encrypt(password)
            self.__update(self.user_table, {'user_password': f'{passwordMd5}'}, {'user_name': f'{userName}'})
            return f'用户：{userName}密码已修改为：{password}'
    
    def queryAllUser(self):
        result = self.__query(self.user_table, None, 'user_name')
        return result

    def deleteUser(self, userName: str) -> None:
        self.__delete(self.user_table, {'user_name': f'{userName}'})

    def queryAllProduct(self):
        result = self.__query(self.prod_table, None, '*')
        return result
    
    def queryAllMaterial(self):
        result = self.__query(self.mat_table, None, '*')
        return result