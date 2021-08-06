import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="")
# db = mysql.connector.connect(host="localhost", user="root", passwd="",database="movies")
cur = db.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS movies")
cur.execute("USE movies")
cur.execute("DROP TABLE IF EXISTS movie")
sql = '''CREATE TABLE movie(ID int NOT NULL PRIMARY KEY,Movie_name varchar(100) NOT NULL,Lead_Actor_Name varchar(100),Lead_Actress_Name varchar(100),Director_Name varchar(100),Release_year int
)'''
cur.execute(sql)
sql = """INSERT INTO movie(ID,Movie_name,Lead_Actor_Name,Lead_Actress_Name,Director_Name,Release_year)VALUES (1,'Kochi Rajavu','Dileep','Kavya','Johny Antony',2005),(2,'Ramaleela','Dileep','Prayaga Martin','Arun Gopy',2017),(3,'Rajamanikyam','Mammootty','Padmapriya','Anwar Rasheed',2005),(4,'Chithram','Mohanlal',' Ranjini','Priyadarshan',1988),(5,'Drishyam','Mohanlal','Meena','Jeethu Joseph',2013),(6,'Anarkali','Prithviraj Sukumaran','Priyal Gor','Sachy',2015),(7,'Malik','Fahad Fasil','Nimisha Sajayan','Mahesh Narayanan',2021),(7,'Captain','Jayasurya','Anu Sithara','Prajesh Sen',2018)"""
try:
    cur.execute(sql)
    db.commit()

except:
    db.rollback()
cur.execute("SELECT * FROM movie")
result = cur.fetchall()
for x in result:
    for y in x:
        print(y)
db.close()