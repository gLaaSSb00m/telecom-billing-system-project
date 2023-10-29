from database import *
from bill_datebase import  b_d
import re
import random
def check_pass(ps0):
    pattern =r'\d{4}$'
    if re.match(pattern,ps0):
        return True
    else :
        return False
def check_number(ref1):
    pattern = r'^01\d{9}$'
    if re.match(pattern, ref1):
        return True
    else:
        return False
def pay(name,id):
    while True:
        f1=f"ENTER YOUR {name} NUMBER: "
        ac_n=input(f1)
        if check_number(ac_n):
            break
        print("Please Enter 11 digit")
        print()
        print()
        print()
    ac_m=0
    while True:
        ac_m=int(input("PLEASE SEND A MINIMUM COST (100TK): "))
        rs=b_d(id)
        
        if(100<=ac_m and rs[0][6]-ac_m>=0):
            break
    rs=b_d(id)
    formula=f"update bill set payment = {ac_m} where id={id}"
    s.execute(formula)
    mydb.commit()
    rs=b_d(id)
    if rs[0][6]!=0:
        a=rs[0][6]-ac_m
        if a>0:
            fom=f"update bill set previous_due={a} where id={1}"
            s.execute(fom)
            mydb.commit()
        elif a==0:
            fom=f"update bill set previous_due={0} where id={1}"
            s.execute(fom)
            mydb.commit()
        else:
            a=rs[0][5]-a
            fom=f"update bill set due={a} where id={1}"
            s.execute(fom)
            mydb.commit()
    ran1=[]
    formula=f"select b_id from bill_details where id={id}"
    s.execute(formula)
    a0=s.fetchall()
    for a1 in a0:
        for a2 in a1:
            ran1.append(a2)
    ran=0
    while True:
        ran=random.randint(1,500)
        if ran not in ran1:
            ran1.append(ran)
            break
    formula=f"insert into bill_details(id,bill_id,bill_receive,b_id) values({id}, {rs[0][1]}, {ac_m},{ran})"
    s.execute(formula)
    mydb.commit()
    rs=b_d(id)
    a1=rs[0][7]-ac_m
    fom=f"update bill_details set due = {a1} where (id,b_id)=({id},{ran})"
    s.execute(fom)
    mydb.commit()
    fom=f"update bill set total_ammount={a1} where id={id}"
    s.execute(fom)
    mydb.commit()
    while True:
        ps0=input("ENTER YOUR ACCOUNT PASSOWRD: ")
        if check_pass(ps0):
            break
        print("ENTER A 4 DIGIT")
    while True:
        ps1=input("ENTER YOUR USER PASSWORD: ")
        formula=f"select password from user where id={id}"
        s.execute(formula)
        rs=s.fetchall()
        if(ps1==rs[0][0]):
            break
    s.execute("select b_id from bill_details where id=1")
    rs=s.fetchall()
    print(rs)
    print()
    print()
    print()
    s.execute("select * from bill where id=1")
    rs=s.fetchall()
    print(rs)