from database import *
#noti=input("ENTER YOUR NOTFICATION: ")
s.execute("insert into notification (id,email) select distinct id,email from user")
mydb.commit()