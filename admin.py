from database import *
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
            """)
        
            press=int(input("Enter Your Input: "))
            if press==1:
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
                            print("ok")
                            #strat

                            while True:
                                password = input("Enter your password: ")

                                s.execute("select password from admin")
                                value=s.fetchall()
                                found=False
                                for t in value:
                                    if password in t:
                                        found=True
                                        break
                                if found:
                                    print("ok")
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
            elif press==2:
                print()
                print()
                create_account()
                break

            else:
                        print("""
                ****************Invalid input,please try again****************
                """)
        except Exception as e:
                print("please enter the int() value, string is not allow ",str(e))
                print()
                print()
                print()
