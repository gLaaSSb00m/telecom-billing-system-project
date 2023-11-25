from database import *
import re

def create_account():
   
    while(True):
        try:
            print('''
          .....................
          . press 1: back     .
          .....................
          . press 2: exit     .
          .....................
          . press 3: continue .
          .....................
''')
            press=int(input("ENTER YOUR INPUT:  "))
            if press == 1:
                from admin import admin
                admin()
            if press == 2:
                exit()
            if press == 3:
                def ref_number(ref1):
                    pattern = r'^\d{4}$'
                    if re.match(pattern, ref1):
                        return True
                    else:
                        return False
                def check_email(email):
                    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                    if re.match(pattern, email):
                        return True
                    else:
                        return False

                def check_username(username):
                    if len(username) >= 4:
                        return True
                    else:
                        return False

                def check_password(password):
                    if len(password) >= 8:
                        return True
                    else:
                        return False

                def check_mobile_number(mobile_number):
                    pattern = r'^01\d{9}$'
                    if re.match(pattern, mobile_number):
                        return True
                    else:
                        return False

                
                ref=1012
                email = input("Enter your email: ")
                while not check_email(email):
                    print("Invalid email address. Please try again.")
                    email = input("Enter your email: ")

                username = input("Enter your username: ")
                while not check_username(username):
                    print("Username should be at least 11 characters long. Please try again.")
                    username = input("Enter your username: ")

                password = input("Enter your password: ")
                while not check_password(password):
                    print("Password should be at least 8 characters long. Please try again.")
                    password = input("Enter your password: ")

                confirm_password = input("Confirm your password: ")
                while password != confirm_password:
                    print("Passwords do not match. Please try again.")
                    confirm_password = input("Confirm your password: ")

                mobile_number = input("Enter your mobile number: ")
                while not check_mobile_number(mobile_number):
                    print("Invalid mobile number. Please try again.")
                    mobile_number = input("Enter your mobile number: ")
                ref1 = input("Enter your refference number(exact 4 digit): ")
                while not ref_number(ref1):
                    print("Invalid refferece number. Please try again.")
                    print()
                    print()
                    ref1 = input("Enter your referrence number(exact 4 digit): ")

                while True:
                    ref = int (input("Enter refference code: "))

                    s.execute("select ref from admin")
                    value=s.fetchall()
                    found=False
                    for t in value:
                        if ref in t:
                            found=True
                            break
                    if found:
                        ref2=int(ref1)
                        formula="insert into admin (name,password,email,mobile,ref) values(%s,%s,%s,%s,%s)"
                        admin1=(username,password,email,mobile_number,ref2)
                        s.execute(formula,admin1)
                        mydb.commit()
                        print("account create successfull")
                        break
                    else:
                        print("""
                            ****************Invalid password,please try again****************
                            """)
                        print()
                        print()
        except Exception as e:
            print(str(e))



