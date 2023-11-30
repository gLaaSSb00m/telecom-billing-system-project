from database import *
#from log_in import log_in
from admin_create_account import create_account
import re
import mysql.connector
conn=mysql.connector.connect(host='localhost',password='Pslle@08',user='root')
def admin():

    while True:
        try:
            print(""" 
        .........................
        .       1- LOG IN       .
        .........................
        .    2- CREATE ACCOUNT  .
        .........................
             3- back            .
        .........................
             4- exit            .
        .........................
            """)
            press=int(input("Enter Your Input: "))
            if press==1:
                while(True):
                     try:
                            print('''
                                1- FOR BACK
                                2- FOR EXIT
                                3- FOR CONTINUE
                            ''')
                            press=int(input("enter your input:  "))
                            if press==1:
                                from admin import admin
                                admin()
                            elif press==2:
                                 exit()
                            elif press==3:
                                 
                                def check_email(email):
                                    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                                    if re.match(pattern, email):
                                        return True
                                    else:
                                        return False
                                while True:
                                    user_email = input("Enter an email address: ")

                                    if check_email(user_email):
                                        #email check
                                        s.execute("select email from admin")
                                        value=s.fetchall()
                                        found=False
                                        for t in value:
                                            if user_email in t:
                                                found=True
                                                break
                                        if found:

                                            while True:
                                                from password import hide_password
                                                password = hide_password()
                                                s.execute("select password from admin")
                                                value=s.fetchall()
                                                found=False
                                                for t in value:
                                                    if password in t:
                                                        found=True
                                                        break
                                                if found:
                                                    from admin_panal import admin_panal
                                                    admin_panal(user_email,password)
                                                    break
                                                else:
                                                    print("""
                                ****************Invalid password,please try again****************
                                """)
                                                    print()
                                                    print()
                                                
                                        
                                            break        
                                            #end
                                        else:
                                            print("""
                                ****************Invalid email address,please try again****************
                                """)
                                        
                                            print()
                                            print()
                                            print()
                                        
                                        
                                    else:
                                        print("""
                                ****************Invalid email address,please try again****************
                                """)
                                        print()
                                        print()
                                        print()
                                break
                     except Exception  as e:
                                print(str(e))
            elif press==2:
                print()
                print()
                create_account()
                break
            elif press==3:
                   from log_in import log_in
                   log_in()
            elif press ==4:
                 exit()
            else:
                        print("""
                ****************Invalid input,please try again****************
                """)
        except Exception as e:
                print("please enter the int() value, string is not allow ",str(e))
                print()
                print()
                print()
