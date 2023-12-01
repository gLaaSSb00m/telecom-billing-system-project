import stat

import setuptools.package_index

from  database import *
from admin_database import *
import re
def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
def admin_panal(email,password):
    while True:
        formula=f"select name from admin where email='{email}' and password={password}"
        s.execute(formula)
        r0=s.fetchall()
        name=r0[0][0]
        try:
            print()
            print()
            print(f'''                  WELCOME MR. {name}
                  
                  
                  
                  PRESS 1: CUSTOMER MANAGEMENT
                  PRESS 2: GENERATE INVOICE
                  PRESS 3: VIEW PAYMENT
                  PRESS 4: CUSTOMER SUPPORT
                  PRESS 5: ADD NEW RECORD
                  PRESS 6: MODIFY RECORD
                  PRESS 7: SERACH RECORD
                  PRESS 8: DELETE RECORD
                  PRESS 9: GENEREATE NOTIFICATION
                  PRESS 10: BACK
                  PRESS 11: EXIT
                ''')
            press=int(input("ENTER YOUR INPUT:  "))
            if press==1:
                s.execute("select * from user")
                r1=s.fetchall()
                t=[]
                for t0 in r1:
                    for t1 in t0:
                        t.append(t1)
                for t0 in range(0,len(t),9):
                    print(f"| {t[t0]} | {t[t0+1]} | {t[t0+2]} | {t[t0+3]} | {t[t0+4]} | {t[t0+5]} | {t[t0+6]} | {t[t0+7]} | {t[t0]+8}")
                while True:
                    print('''
                          PRESS 1: FOR CHANGE ID
                          PRESS 2: FOR CHANGE NAME
                          PRESS 3: FOR CHANGE EMAIL
                          PRESS 4: FOR CHANGE TELEPHONE
                          PRESS 0: FOR BACK
                        ''')
                    press=int(input("enter your input: "))
                    if press==1:
                        i=0
                        id=0
                        try:
                            while True:
                                try:
                                    i=0
                                    id=int(input("ENTER  USER ID NUMBER: "))
                                    e=input("ENTER USER EMAIL : ")
                                    f1=f"select id,email from user where (id,EMAIL)=({id},'{e}')"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        if id==r1[0] and e==r1[1]:
                                            i=1
                                            break
                                    if i==1:
                                        break
                                    print("INVALID ID")
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            id1=0
                            id2=0
                            while True:
                                try:
                                    k=0
                                    id1=int(input("ENTER NEW ID NUMBER: "))
                                    id2=int(input("ENTER CONFIRM ID NUMBER: "))
                                    if id1==id2:  
                                        s.execute("select id from user")
                                        r=s.fetchall()
                                        for r1 in r:
                                            for r2 in r1:
                                                if id1 == r2:
                                                    k=1
                                                    break
                                    if(k==0 and id1==id2):
                                        break
                                    elif k==1:
                                        print("this id is already exsits")
                                    elif id1!=id2:
                                        print("NO match")
                                        
                                    print()
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            rs=u_id(id)
                            formula=f"update user set id= {id1} where (email,nid,telephone)=('{rs[0][0]}','{rs[0][1]}','{rs[0][2]}')"
                            s.execute(formula)
                            mydb.commit()
                        except Exception as e:
                            print(str(e)) 
                    elif press==2:
                        id=0
                        e=""
                        while True:
                            try:
                                i=0
                                i1=0
                                id=int(input("ENTER  ID NUMBER: "))
                                e=input("ENTER EMAIL : ")
                                f1=f"select id,email from user where (id,email)=({id},'{e}')"
                                s.execute(f1)
                                r=s.fetchall()
                                for r1 in r:
                                    if id==r1[0] and e==r1[1]:
                                        i=1
                                        break
                                if i==1:
                                    f1=f"select name from user where (id,email)=({id},'{e}')"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        print(r1[0])
                                    break
                                print("INVALID ID")
                                print()
                                print()    
                            except Exception as e:
                                print(str(e))
                        nam=input("ENTER USER NEW NAME: ")
                        f1=f"update user set name='{nam}' where (id,email)=({id},'{e}')"
                        s.execute(f1)
                        mydb.commit()    
                        break
                    elif press==3:
                        i=0
                        id=0
                        try:
                            while True:
                                try:
                                    i=0
                                    id=int(input("ENTER  ID NUMBER: "))
                                    e=input("ENTER NID NUMBER : ")
                                    f1=f"select id,NID from user where (id,NID)=({id},'{e}')"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        if id==r1[0] and e==r1[1]:
                                            i=1
                                            break
                                    if i==1:
                                        break
                                    print("INVALID ID")
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            id1=0
                            id2=0
                            while True:
                                try:
                                    k=0
                                    id1=input("ENTER NEW USER EMAIL: ")
                                    while not check_email(id1):
                                        print("Invalid email address. Please try again.")
                                        id1 = input("ENTER NEW USER EMAIL: ")
                                    id2=input("ENTER CONFIRM USER EMAIL: ")
                                    while not check_email(id2):
                                        print("Invalid email address. Please try again.")
                                        id2 = input("ENTER CONFIRM USER EMAIL: ")
                                    if id1==id2:  
                                        s.execute("select email from user")
                                        r=s.fetchall()
                                        for r1 in r:
                                            for r2 in r1:
                                                if id1 == r2:
                                                    k=1
                                                    break
                                    if(k==0 and id1==id2):
                                        break
                                    elif k==1:
                                        print("this email is already exsits")
                                    elif id1!=id2:
                                        print("NO match")
                                        
                                    print()
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            rs=u_email(id)
                            formula=f"update user set email= '{id1}' where (id,nid,telephone)=('{rs[0][0]}','{rs[0][1]}','{rs[0][2]}')"
                            s.execute(formula)
                            mydb.commit()
                        except Exception as e:
                            print(str(e)) 


                    elif press==4:
                        i=0
                        id=0
                        try:
                            while True:
                                try:
                                    i=0
                                    id=int(input("ENTER  USER ID NUMBER: "))
                                    e=input("ENTER USER EMAIL : ")
                                    f1=f"select id,email from user where (id,EMAIL)=({id},'{e}')"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        if id==r1[0] and e==r1[1]:
                                            i=1
                                            break
                                    if i==1:
                                        break
                                    print("INVALID ID")
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            id1=0
                            id2=0
                            while True:
                                try:
                                    k=0
                                    id1=input("ENTER NEW TELEPHONE NUMBER: ")
                                    id2=input("ENTER CONFIRM TELEPHONE NUMBER: ")
                                    if id1==id2:  
                                        s.execute("select TELEPHONE from user")
                                        r=s.fetchall()
                                        for r1 in r:
                                            for r2 in r1:
                                                if id1 == r2:
                                                    k=1
                                                    break
                                    if(k==0 and id1==id2):
                                        break
                                    elif k==1:
                                        print("this id is already exsits")
                                    elif id1!=id2:
                                        print("NO match")
                                        
                                    print()
                                    print()
                                    print()
                                except Exception as e:
                                    print(str(e))
                            rs=u_telephone(id)
                            formula=f"update user set telephone= '{id1}' where (id,nid,email)=('{rs[0][0]}','{rs[0][1]}','{rs[0][2]}')"
                            s.execute(formula)
                            mydb.commit()
                        except Exception as e:
                            print(str(e))

                    elif press==0:
                        from admin_panal import admin_panal
                        admin_panal()



                
            elif press ==2:
                try:
                    noti=input("ENTER YOUR NOTFICATION: ")
                    s.execute("insert into noti1 (id,email) select distinct id,email from user")
                    mydb.commit()
                    formula=f'''with noti as (select distinct id from notification) update notification set notificationcol='{noti}'  where id in 
                    (select distinct id from noti)'''
                    s.execute(formula)
                    mydb.commit()
                except Exception as e:
                    print(str(e))

            elif press ==3:
                try:
                    i=input("ENTER USER ID/ALL: ")
                    if i.lower()=="all":    
                        s.execute("select id,bill_id as BILL_NO, payment from bill")
                        rs=s.fetchall()
                        for rs1 in rs:
                            print(f"|{rs1[0]} | {rs1[1]} | {rs1[2]}")
                    else:
                        i=int(i)
                        formula=f"select id, BILL_ID AS BILL_NO, payment from BILL where id={i}"
                        s.execute(formula)
                        rs=s.fetchall()
                        for rs1 in rs:
                            print(f"|{rs1[0]} | {rs1[1]} | {rs1[2]}")
                except Exception as e:
                    print(str(e))
            elif press==4:
                try:
                    i=input("ENTER USER ID/ALL: ")
                    if i.lower()=="all":    
                        s.execute("select id,feedback as Customer_Report from feedback")
                        rs=s.fetchall()
                        for rs1 in rs:
                            print(f"|{rs1[0]} | {rs1[1]} | {rs1[2]}")
                    else:
                        i=int(i)
                        formula=f"select id, feedback as Customer_Report from feedback where id={i}"
                        s.execute(formula)
                        rs=s.fetchall()
                        for rs1 in rs:
                            print(f"|{rs1[0]} | {rs1[1]} | {rs1[2]}")
                except Exception as e:
                    print(str(e))

            elif press ==5:
                try:
                    i=int(input("ENTER USER ID: "))
                    bill_id=int(input("ENTER BILL ID: "))
                    last_date=input(f"ENTER LAST DATE(%yy-%mm-%dd): ")
                    ammount=float(input("ENTER YOUR AMMOUNT: "))
                    late_fee=float(input("ENTER USER LATE FEE: "))
                    due=float(input("ENTER USER DUE: "))
                    previous_due=float(input("ENTER USER PREVIOUS DUE: "))
                    total_ammount=float(input("ENTER TOTAL AMMOUNT: "))
                    payment=float(input("ENTER USER PAYMENT: "))
                    formula=f"insert into bill(id,bill_id, last_date, ammount, late_fee, due, previous_due, total_ammount, payment) values ({i},{bill_id},'{last_date}',{ammount},{late_fee},{due},{previous_due},{total_ammount}, {payment} )"
                    s.execute(formula)
                    mydb.commit()

                except Exception as e:
                    print(str(e))
            elif press==6:
                try:
                    i=int(input("ENTER ID: "))
                    se=f"select * from bill where id={i}"
                    s.execute(se)
                    rs=s.fetchall()
                    for rs1 in rs:
                        
                        print(f"| id: {rs1[0]} | bill_id: {rs1[1]} | last_date: {rs1[2]} | ammount: {rs1[3]} | late_fee: {rs1[4]} | due: {rs1[5]} | previous_due: {rs1[6]} | total_ammount: {rs1[7]} | payment: {rs1[8]} |")
                    while True:

                        col=input("ENTER MODIFY COLUMN(last_date, ammount, late_fee, due, previous_due, total_ammount, payment): ")
                        data=input("ENTER YOUR DATA: ")
                        bill_id=int(input("enter a bill id: "))
                        if col.lower() in ["last_date"]:
                            up=f"update bill set {col}='{data}' where id={i}"
                            s.execute(up)
                            mydb.commit()
                            break
                        elif col.lower() in ["ammount","last_fee","due","previous_due","total_ammount","payment"]:
                            data=int(data)
                            up=f"update bill set {col}={data} where (id,bill_id)=({i},{bill_id})"
                            s.execute(up)
                            mydb.commit()
                            break
                        else:
                            print("please enter a correct column")
                        
                except Exception as e:
                    print(str(e))
            elif press==7:
                try:
                    i=int(input("ENTER ID: "))
                    se=f'''SELECT user.id,user.name,user.password, user.email, user.TELEPHONE, user.nid, user.REGISTRATION_DATE, 
bill.BILL_ID, bill.LAST_DATE, bill.AMMOUNT, bill.LATE_FEE,bill.due,bill.previous_due, bill.TOTAL_AMMOUNT,bill.payment
FROM user
JOIN bill ON user.id = bill.id and user.id= {i};
'''
                    s.execute(se)
                    rs=s.fetchall()
                    for rs1 in rs:
                        print(f"| id: {rs1[0]} | name: {rs1[1]} | password: {rs1[2]} | email: {rs1[3]} | telephone: {rs1[4]} | nid: {rs1[5]} | registration_date: {rs1[6]} | bill_id: {rs1[7]} | last_date: {rs1[8]} | ammount: {rs1[9]} | late_fee: {rs1[10]} | due: {rs1[11]} | previous_due: {rs1[12]} | total_ammount: {rs1[13]} | payment: {rs1[14]} |")
                        print()
                        print()
                except Exception as e:
                    print(str(e))
            elif press==8:
                try:
                    i=int(input("ENTER USER ID: "))
                    se=f"select * from bill where id={i}"
                    s.execute(se)
                    rs=s.fetchall()
                    for rs1 in rs:
                        
                        print(f"| id: {rs1[0]} | bill_id: {rs1[1]} | last_date: {rs1[2]} | ammount: {rs1[3]} | late_fee: {rs1[4]} | due: {rs1[5]} | previous_due: {rs1[6]} | total_ammount: {rs1[7]} | payment: {rs1[8]} |")
                    b_id=int(input("ENTER USER BILL ID: "))
                    de=f"delete from bill where (id,bill_id)=({i},{b_id})"
                    s.execute(de)
                    mydb.commit()
                except Exception as e:
                     print(str(e))

            elif press==9:
                def check_id(id,e):
                    f=f"select email from id={id} "
                    s.execute(f)
                    r1=s.fetchall()
                    if r1[0][1]==e:
                        return True
                    else:
                        return False
                try:
                    while(True):
                        f=f"select id,name,email from user"
                        s.execute(f)
                        r1=s.fetchall()
                        for r2 in r1:
                            print(f'''
                            id: {r2[0]} | name: {r[1]}  |   email: {r2[2]}
''')
                        id=int(input("ENTER USER ID: "))
                        e=input("ENTER USER EMAIL:  ")
                        if check_id(id,e):
                            noti=input("ENTER NOTIFICATION:    ")
                            f=f"insert into noti1 values({id},'{e}','{noti}')"
                            s.execute(f)
                            mydb.commit()
                            break
                        else:
                            print("---------------invalid account--------------")        
                except Exception as e:
                    print(str(e))
                
            elif press==10:
                from admin import admin
                admin()
            elif press==11:
                exit()
            
        except Exception as e:
            print("PLEASE ENTER  NUMBER",str(e))

admin_panal("eaabid1012@gmail.com",1012)