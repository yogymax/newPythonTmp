import pymysql


connection = pymysql.connect(user='root',password='admin123',db='sample',port=3306,host='localhost')
print(connection)

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor = connection.cursor()

mysql_INsertQuery = '''
                insert into employee values('Abcd','PQR',22,'M',12312)
            '''

cursor.execute(sql)
