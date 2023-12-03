from database import *
#noti=input("ENTER YOUR NOTFICATION: ")
try:
    s.execute("select password from admin where email='mdazadhossainrazu@gmail.com'")
    rs=s.fetchall()
    for i in rs:
        print(i)
except Exception as e:
    print(str(e))