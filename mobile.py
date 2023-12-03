from database import *
for i in range(20,23):
    print(f"for id {i}")
    pas=input("enter number: ")
    f=f"update user set nid='{pas}' where id={i}"
    s.execute(f)
    mydb.commit()