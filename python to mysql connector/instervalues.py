import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='haresh@123',database='pythondb')
mycursor = conn.cursor()

sql = 'insert into student1(name,branch,id) values(%s,%s,%s)'

value=[('haresh','cse',1),('suresh','aiml',2),('rajesh','it',3),('mahesh','ds',4),('ramesh','cs',5)]

mycursor.executemany(sql,value)
conn.commit()
print(mycursor.rowcount,"record inserted")