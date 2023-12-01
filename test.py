

from database import *
try:
    id=1
    email="eaabid@gmail.com"
    noti="aaw"
    f=f"insert into noti1 values({id},'{email}','{noti}')"
    s.execute(f)
    mydb.commit()
except Exception as e:
    print(str(e))