#!C:\Users\PC\AppData\Local\Programs\Python\Python39\python.exe
print("Content-type:text/html\r\n\r\n")

import mysql.connector
import cgi


form = cgi.FieldStorage()


n = form.getvalue("fullname")
p = form.getvalue("phonenumber")
e = form.getvalue("emailname")
g = form.getvalue("gender")
d = form.getvalue("dob")
rn = form.getvalue("rno")
ss = form.getvalue("ssemester")
grid = form.getvalue("gridCheck")

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'information'    # Database Name Changable
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (student_name,phone_number,email,gender,date_of_birth,reg_no,semister,submit_info) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" # Tabel Name And Table Column Name Changable
val = (n,p,e,g,d,rn,ss,grid)


mycursor.execute(sql,val)
mydb.commit()
mydb.close()
print("<h2 style='color:#20b531;'>Successfully</h2>")
print(mycursor.rowcount,"Record Inserted")

print("<h1><a href='http://localhost/asp/index.html' style='text-decoration:none;'>Back Home Page</a></h1>")

# This asp name folder changable 
