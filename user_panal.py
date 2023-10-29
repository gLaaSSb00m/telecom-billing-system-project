from database import *
from bill_datebase import b_d
from datetime import date
from payment import pay
import re
def check_s(string):
    pattern = r'^.{1,250}$'  # Matches strings with 1 to 250 characters
    if re.search(pattern, string):
        return True
    else:
        return False
def user_panal(email):
    while True:
        formula="select * from user where email=%s"
        s.execute(formula,(email,))
        id1=s.fetchall()
        id=id1[0][0]
        name=id1[0][1]
        rs=b_d(id)
        late_fee=0
        total_amount=0
        l=0
        if rs[0][2]<date.today() and rs[0][5]!=0:
            rs=b_d(id)
            late_fee=float(rs[0][5])*(5/100)
            print(late_fee)
            formula=f"update bill set late_fee={late_fee} where id={id}"
            s.execute(formula)
            mydb.commit()
            l+=1
        if rs[0][2]<date.today() and rs[0][5]!=0:
            rs=b_d(id)
            total_amount=rs[0][4]+rs[0][5]+rs[0][6]
            formula=f"update bill set total_ammount={total_amount} where id = {id}"
            s.execute(formula)
            mydb.commit()
        rs=b_d(id)
        if l==1:
            no= "YOUR PAYMENT IS DUE,    PLEASE PAY YOUR DUE"
            l=0
        formula="select notificationcol from notification where (id,email)=(%s,%s)"    
        s.execute(formula,(id,email))
        l1=s.fetchall()
        for l2 in l1:
            l+=len(l2)

        try:        
            print(f'''                MR. {name} thanks to you for using this platform
                                            
                                        PRESS 1: CALL RECORD
                                        PRESS 2: BILL RECORD
                                        PRESS 3: BILL HISTORY
                                        PRESS 4: PAYMENT 
                                        PRESS 5: CONTACT US
                                        PRESS 6: ABOUT US
                                        PRESS 7: FEEDBACK
                                        PRESS 8: INFORMATION
                                        PRESS 9: YOU HAVE {l} NOTIFICATION
                                        PRESS 10: HISTORY OF NOTIFICATION

                                        
                                        
                                        {no}
                ''')
    
            press=int(input("ENTER YOUR INPUT: "))
            if press==1:
                
                formula1="select call_id, call_date, duration from call_details where id=%s"
                s.execute(formula1,(id,))
                r=s.fetchall()
                r3=[]
                for r1 in r:
                    for r2 in r1:
                        r3.append(r2)
                for li in range(0,len(r3),3):
                    print(f'''

                    | NUMBER: {r3[li]}    |  DATE & TIME: {r3[li+1]} | DURATION: {r3[li+2]} |

                    ''')
                
            elif press==2:
                rs=b_d(id)
                print(f'''
                | BILL ID: {rs[0][1]} | LASTE DATE: {rs[0][2]} | AMOUNT: {rs[0][3]} | LATE FEE: {rs[0][4]} | DUE: {rs[0][5]} | PREVIOUS DUE: {rs[0][6]} | TOTAL AMOUNT: {rs[0][7]} | PAYMENT: {rs[0][8]} |
                ''')
            elif press==3:
                formula="select bill_id, BILL_RECEIVE, DUE, RECEIVE_DATE from bill_DETAILS where id=%s order by receive_date;"
                s.execute(formula,(id,))
                r=s.fetchall()
                s2=[]
                for s0 in r:
                    for s1 in s0:
                        s2.append(s1)
                for r1 in range(0,len(s2),4):    
                    print(f'''
                | BILL ID: {s2[r1]} | BILL RECEIVE: {s2[r1+1]} | DUE: {s2[r1+2]} | RECEIVE DATE: {s2[r1+3]} |   
                    ''')
                
            elif press==4:
                print('''WHICH ACCOUNT ARE YOU CHOOSE: 
                                                        1.BKASH
                                                        2.NAGAD
                                                        3.ROCKET''')
                p=int(input("ENTER YOUR INPUT: "))
                if p==1:
                    pay("BKASH",1)
                    
                elif p==2:
                    pay("NAGAD", id)
                elif p==3:
                    pay("ROCKET", id)
            elif press ==5:
                print("contact us")
            elif press ==6:
                print("about us")
            elif press ==7:
                while True:
                    print("at most 250 character")
                    feed=input()
                    if check_s(feed):
                        break
                    print()
                    print()
                    print()
                formula="insert into feedback (id,email,feedback)  values(%s,%s)"
                s.execute(formula,(id,email,feed))
                mydb.commit()
            elif press==9:
                    formula="select  notificationcol from notification where (id,email)=(%s,%s)"
                    s.execute(formula,(id,email,))
                    n1=s.fetchall()
                    # print(f"{name} {id} {email}")
                    # print(n1)
                    k=[]
                    for n2 in n1:
                        for n3 in n2:
                            k.append(n3)
                    for k1 in k:
                        print(k1)
                                            
                    f1="insert into history_notification select * from notification where (id,email)=(%s,%s)"
                    s.execute(f1,(id,email,))
                    mydb.commit()
                    f1="delete from notification where (id,email)=(%s,%s)"
                    s.execute(f1,(id,email,))
                    mydb.commit()
            elif press==10:
                f1="select history_notificationcol from history_notification where (id,email)=(%s,%s)"
                s.execute(f1,(id,email))
                n1=s.fetchall()
                    # print(f"{name} {id} {email}")
                    # print(n1)
                k=[]
                for n2 in n1:
                    for n3 in n2:
                        k.append(n3)
                for k1 in k:
                    print(k1)

        except Exception as e:
            print("sorry please enter a int number",str(e))
            print()
            print()
            print()
