from database import *
for i in range(1,22):
    print(f"for id {i}")
    pas=input("enter pass: ")
    f=f"update user set password='{pas}' where id={i}"
    s.execute(f)
    mydb.commit()