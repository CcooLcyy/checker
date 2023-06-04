import pymysql
import hashlib


class Mysql():
    def __init__(self):
        self.user_table = 'users'
        self.prod_table = 'products'
        self.mat_table = 'materials'
        self.bom_table = 'boms'
        self.mark_table = 'marks'
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='checker',
                password='password',
                database='checker'
            )
            self.installed = True
            if self.connection != None:
                self.cursor = self.connection.cursor()
            if not self.userExist('admin'):
                self.__insert(self.user_table, {
                    'user_id': '1',
                    'user_name': 'admin',
                    'user_password': f"{self.md5_encrypt('admin')}"})
                self.__init__()
        except Exception as e:
            if e.args[0] == 2003:
                self.installed = False
            elif e.args[0] == 1146:
                self.__createTable(self.user_table,
                                   {
                                       'user_id': 'INT(32) AUTO_INCREMENT PRIMARY KEY',
                                       'user_name': 'CHAR(32)',
                                       'user_password': 'CHAR(32)'
                                   },
                                   False)
                self.__createTable(self.prod_table,
                                   {
                                       'prod_id': 'INT(32) PRIMARY KEY',
                                       'prod_name': 'CHAR(32)'
                                   },
                                   False)
                self.__createTable(self.mat_table, {
                    'mat_id': 'INT(32) PRIMARY KEY',
                    'mat_name': 'CHAR(32)'}, False)
                self.__createTable(self.bom_table, {
                    'prod_id': 'INT(32)',
                    'mat_id': 'INT(32)'}, True)
                self.__createTable(self.mark_table,
                                   {
                                       'classed_id': 'CHAR(32) PRIMARY KEY',
                                       'mat_id': 'INT(32)',
                                       'prod_id': 'INT(32)',
                                       'user_name': 'CHAR(32)',
                                       'mark_time': 'DATETIME DEFAULT CURRENT_TIMESTAMP',
                                       'a_class': 'BOOL',
                                       'b_class': 'BOOL',
                                       'c_class': 'BOOL'
                                   }, True)
            elif e.args[0] == 1049:
                self.connection = pymysql.connect(
                    host='localhost',
                    user='checker',
                    password='password',
                )
                self.cursor = self.connection.cursor()
                self.cursor.execute('CREATE DATABASE checker;')
                self.cursor.execute('ALTER DATABASE checker '
                                    'CHARACTER SET utf8mb4 '
                                    'COLLATE utf8mb4_general_ci;')
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
            conditionsStr = ' AND '.join([
                f"{key} = '{value}'"
                for key, value in conditions.items()])
            sql = f"SELECT {columnsStr} FROM {tableName} WHERE {conditionsStr}"
            self.cursor.execute(sql)
        else:
            sql = f"SELECT {columnsStr} FROM {tableName}"
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __subQuery(self, tableName, subTableName, conditions=None, subConditions=None, *subColumnNames):
        subQueryResult = ', '.join([str(x[0]) for x in self.__query(
            subTableName, subConditions, *subColumnNames)])
        if conditions:
            conditionsStr = ' AND '.join(
                [f"{key} = %s" for key in conditions.keys()])
            sql = f"SELECT * FROM {tableName} WHERE {conditionsStr} AND {subColumnNames[0]} IN ({subQueryResult})"
            values = tuple(conditions.values())
            self.cursor.execute(sql, values)
        else:
            sql = f"SELECT * FROM {tableName} WHERE {subColumnNames[0]} IN ({subQueryResult})"
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def __createTable(self, tableName, columns, foreign=None):
        columnsStr = ', '.join([
            f"{columnName} {columnType}"
            for columnName, columnType in columns.items()])
        sql = f"CREATE TABLE {tableName} ({columnsStr}"
        if foreign:
            sql = sql + \
                ', FOREIGN KEY (prod_id) REFERENCES products(prod_id) ON DELETE CASCADE,'
            sql = sql + \
                'FOREIGN KEY (mat_id) REFERENCES materials(mat_id) ON DELETE CASCADE)'
        else:
            sql = sql + ')'
        self.cursor.execute(sql)
        self.connection.commit()

    def __update(self, tableName, data, condition):
        setValues = ', '.join([f"{key} = %s" for key in data.keys()])
        conditionStr = ' AND '.join(
            [f"{key} = %s" for key in condition.keys()])
        sql = f"UPDATE {tableName} SET {setValues} WHERE {conditionStr}"
        values = list(data.values()) + list(condition.values())
        self.cursor.execute(sql, values)
        self.connection.commit()

    def __delete(self, tableName, conditions=None):
        value = ()
        if conditions:
            conditionStr = ' AND '.join(
                [f"{key} = %s" for key in conditions.keys()])
            sql = f"DELETE FROM {tableName} WHERE {conditionStr}"
            value = tuple(conditions.values())
        else:
            sql = f"DELETE FROM {tableName}"
        self.cursor.execute(sql, value)
        self.connection.commit()

    def md5_encrypt(self, text: str) -> str:
        msg = hashlib.md5()
        msg.update(text.encode('utf-8'))
        return msg.hexdigest()

    def userExist(self, userName: str):
        result = self.__query(
            self.user_table, {'user_name': f'{userName}'}, 'user_name')
        if len(result) == 0:
            return False
        elif result[0][0] == userName:
            return True

    def verifyPassword(self, userName):
        result = self.__query(
            self.user_table, {'user_name': f'{userName}'}, 'user_password')
        if len(result) != 0:
            return result[0][0]

    def addUser(self, userName, password):
        passwordMd5 = self.md5_encrypt(password)
        if self.__query(self.user_table, {'user_name': f'{userName}', 'user_password': f'{passwordMd5}'}, 'user_name'):
            return '用户存在'
        else:
            self.__insert(self.user_table, {
                          'user_name': f'{userName}', 'user_password': f'{passwordMd5}'})
            return f'用户：{userName}添加成功，密码为：{password}'

    def changePassword(self, userName, password):
        if not self.userExist(userName):
            return '用户不存在，请先添加用户'
        else:
            passwordMd5 = self.md5_encrypt(password)
            self.__update(self.user_table, {'user_password': f'{passwordMd5}'}, {
                          'user_name': f'{userName}'})
            return f'用户：{userName}密码已修改为：{password}'

    def queryAllUser(self):
        result = self.__query(self.user_table, None, 'user_name')
        return result

    def queryAllProduct(self):
        result = self.__query(self.prod_table, None, '*')
        return result

    def queryAllMaterial(self):
        result = self.__query(self.mat_table, None, '*')
        return result

    def queryAllTime(self):
        result = self.__query(self.mark_table, None, 'mark_time')
        return result

    def queryAMarks(self):
        return self.__queryMarksByClass('a_class')

    def queryBMarks(self):
        return self.__queryMarksByClass('b_class')

    def queryCMarks(self):
        return self.__queryMarksByClass('c_class')

    def __queryMarksByClass(self, mark):
        result = self.__query(self.mark_table, None, mark)
        return result

    def queryProdIdByProdName(self, prodName):
        result = self.__query(
            self.prod_table, {'prod_name': prodName}, 'prod_id')
        return result

    def queryMatIdByName(self, matName):
        result = self.__query(self.mat_table, {'mat_name': matName}, 'mat_id')
        return result

    def queryBomByProdId(self, prodId):
        result = self.__query(self.bom_table, {'prod_id': prodId}, 'mat_id')
        return result

    def queryMatNameByID(self, matId):
        result = self.__query(self.mat_table, {'mat_id': matId}, 'mat_name')
        return result

    def queryMarkByConditions(self, userName, prodId, matId, markTime, a, b, c):
        sql = f'SELECT t1.classed_id, t2.prod_name, t3.mat_name, t1.user_name, t1.mark_time, t1.a_class, t1.b_class, t1.c_class FROM marks AS t1 LEFT JOIN products AS t2 ON t1.prod_id = t2.prod_id LEFT JOIN materials AS t3 ON t1.mat_id = t3.mat_id'
        if userName != '*' or prodId != '*' or matId != '*' or a != '*' or markTime != '*':
            sql += ' WHERE'
            if userName != '*':
                sql += f' t1.user_name = {userName} AND'
            if prodId != '*':
                sql += f' t1.prod_id = {prodId} AND'
            if matId != '*':
                sql += f' t1.mat_id = {matId} AND'
            if markTime != '*':
                sql += f' DATE(mark_time) = "{markTime}" AND'
            if a != '*':
                sql += f' t1.a_class = {a} AND t1.b_class = {b} AND t1.c_class = {c}'

        if sql[-3:] == 'AND':
            sql = sql[:-3]

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
    
    def queryMarkByName(self, name):
        result = self.__query(self.mark_table, {'classed_id': f'{name}'}, 'a_class', 'b_class', 'c_class')
        return result

    def addProdMatRow(self, type, value):
        if type == 'prod':
            result = {'prod_id': value[0], 'prod_name': value[1]}
            self.__insert(self.prod_table, result)
        elif type == 'mat':
            result = {'mat_id': value[0], 'mat_name': value[1]}
            self.__insert(self.mat_table, result)

    def addToBom(self, inserRow):
        result = {'prod_id': inserRow[0], 'mat_id': inserRow[1]}
        self.__insert(self.bom_table, result)

    def insertMarkData(self, classId, matId, prodId, userName, aClass, bClass, cClass):
        self.__insert(self.mark_table, {'classed_id': classId, 'mat_id': matId, 'prod_id': prodId,
                      'user_name': userName, 'a_class': aClass, 'b_class': bClass, 'c_class': cClass})

    def deleteBomByProdId(self, prodId):
        self.__delete(self.bom_table, {'prod_id': prodId})

    def deleteUser(self, userName: str) -> None:
        self.__delete(self.user_table, {'user_name': f'{userName}'})

    def deleteProdMatRow(self, type, value):
        if type == 'prod':
            self.__delete(self.prod_table, {'prod_id': f'{value}'})
        elif type == 'mat':
            self.__delete(self.mat_table, {'mat_id': f'{value}'})
