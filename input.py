import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="project"
)
s=mydb.cursor()
while(True):
    print('''
                1 for admin
                2 for bill
                3 for bill_detais
                4 for call_details
                5 for feedback
                4 for history_notification
                6 for notification
                7 for user''')
    p=int(input("enter > "))
    if p==1:
        while(True):
            a=input("enter name ")
            if a=="break":
                break
            b=input("enter password ")
            if b=="break":
                break
            c=input("enter email    ")
            if c=="break":
                break
            d=input("enter mobile   ")
            if d=="break":
                break
            e=input("enter ref  ")
            if e=="break":
                break
            e=int(e)
            f=f"insert into admin (name, password, email, mobile, ref) values ('{a}','{b}','{c}','{d}',{e})"
            s.execute(f)
            mydb.commit()
    if p==2:
        while(True):
            a=input("enter id   ")
            if a=="break":
                break
            b=input("enter bill_id  ")
            if b=="break":
                break
            c=input("enter last_date(yy-mm-dd)    ")
            if c=="break":
                break
            d=input("enter ammout   ")
            if d=="break":
                break
            e=input("enter late_fee   ")
            if e=="break":
                break
            f=input("enter due   ")
            if f=="break":
                break
            g=input("enter previous_due   ")
            if g=="break":
                break
            h=input("enter total_ammount   ")
            if h=="break":
                break
            i=input("enter payment   ")
            if i=="break":
                break
            j=f"insert into bill (id, bill_id, last_date, ammount, late_fee, due, previous_due, total_ammount, payment) values ({a},{b},'{c}',{d},{e},{f},{g},{h},{i})"
            s.execute(j)
            mydb.commit()
    if p==3:
        while(True):
            a=input("enter id(ref) ")
            if a=="break":
                break
            b=input("enter bill_id(ref) ")
            if b=="break":
                break
            c=input("enter bill_receive    ")
            if c=="break":
                break
            d=input("enter due   ")
            if d=="break":
                break
            a=int(a)
            b=int(b)
            c=int(c)
            d=int(d)
            f=f"insert into admin (id, bill_id, bill_receive, due) values ({a},{b},{c},{d})"
            s.execute(f)
            mydb.commit()
    if p==4:
        while(True):
            a=input("enter id(ref) ")
            if a=="break":
                break
            b=input("enter call_id ")
            if b=="break":
                break
            c=input("enter call_date(yy-mm-dd hh:mm:ss)    ")
            if c=="break":
                break
            d=input("enter duration(hh:mm:ss)   ")
            if d=="break":
                break
            f=f"insert into admin (id, call_id, call_date, duration) values ({a},'{b}','{c}','{d}')"
            s.execute(f)
            mydb.commit()