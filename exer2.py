import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="127.0.0.1",
  user ="hongpc",
  passwd ="Hongpc@123##",
  auth_plugin='mysql_native_password'
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE hongsteav")

# creating table 
studentRecord = """CREATE TABLE STUDENT (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
print(studentRecord)


