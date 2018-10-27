import sqlite3
import pymysql

class DatabaseUtil:

    connection = None

    @staticmethod
    def getConnetion(flag=True):
        if DatabaseUtil.connection == None:
            if flag == False:
                DatabaseUtil.connection=sqlite3.connect('empinfo.db')
            else:
                DatabaseUtil.connection = pymysql.connect(user='root',password='admin123',db='sample',port=3306,host='localhost')
        return DatabaseUtil.connection


    @staticmethod
    def createEmpLoyeeTable():
        DatabaseUtil.connection.cursor().execute('''CREATE TABLE EmployeeInfo
                 (EMPID INT PRIMARY KEY     NOT NULL,
                 EMPNAME           TEXT    NOT NULL,
                 EMPAGE            INT     NOT NULL,
                 EMPADDRESS        CHAR(50),
                 EMPSALARY         REAL);''')
        print('Table Create Successfully..')