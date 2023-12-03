from database import *
import re
from user_create_account import user_create_account
from user_panal import user_panal
import maskpass
def user():

    while True:
        try:
            print(""" 
        .........................
        .       1- LOG IN       .
        .........................
        .    2- CREATE ACCOUNT  .
        .........................
        .    3- back            .
        .........................
        .    4-exit             .
        .........................
            """)
        
            press=int(input("Enter Your Input: "))
            if press==1:
                while(True):
                    try:
                        print('''
                            1: FOR BACK
                            2: FOR EXIT
                            3: CONTINUE
                        ''')
                        press=int(input("ENTER THE INPUT: "))
                        if press==1:
                            from user import user
                            user()
                        elif press==2:
                            exit()
                        elif press==3:

                            def check_email(email):
                                pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                                if re.match(pattern, email):
                                    return True
                                else:
                                    return False
                            def check_password(password):
                # Check if the password contains at least one special character, one digit, and one capital letter
                                if not re.search(r'^(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d)(?=.*[A-Z]).{8,}$', password):
                                    return False

                                return True


                            while True:
                                user_email = input("Enter an email address: ")

                                if check_email(user_email):
                                    #email check
                                    s.execute("select email from user")
                                    value=s.fetchall()
                                    found=False
                                    for t in value:
                                        if user_email in t:
                                        
                                            found=True
                                            break
                                    if found:
                                        pass
                                        #strat

                                        while True:
                                            # start
                                            
                                            # Example usage
                                            while True:
                                                entered_password = maskpass.askpass("Enter your password: ",mask='*')
                                                #entered_password=input("enter password:  ")
                                                if check_password(entered_password):
                                                    break
                                                else:
                                                    print("Password must be at least 1 special character, 1 digit, 1 capital letter")

                                            #end
                                            s.execute("SELECT password FROM user")
                                            rows = s.fetchall()
                                            found = False
                                            for row in rows:
                                                password_from_db = row[0]  # Access the first (and only) element of the tuple
                                                if entered_password == password_from_db:
                                                    found = True
                                                    break

                                            if found:
                                                from user_panal import user_panal
                                                user_panal(user_email)
                                            else:
                                                print("""
                            ****************Invalid password,please try again****************
                            """)
                                                print()
                                                print()
                                                print('''
                                                             PRESS 1: FOR BACK
                                                             PRESS 2: FOR EXIT
                                                             PRESS 3: FOR CONTINUE''')
                                                p1=int(input("ENTER YOUR INPUT: "))
                                                if p1==1:
                                                        from admin import user
                                                        user()
                                                if p1==2:
                                                    exit()
                                        break
                                        
                                        #end
                                    else:
                                        print("""
                            ****************Invalid email address,please try again1****************
                            """)
                                    
                                        print()
                                        print()
                                        print()
                                        print('''
                                                             PRESS 1: FOR BACK
                                                             PRESS 2: FOR EXIT
                                                             PRESS 3: FOR CONTINUE''')
                                        p1=int(input("ENTER YOUR INPUT: "))
                                        if p1==1:
                                            from admin import user
                                            user()
                                        if p1==2:
                                            exit()
                                    
                                else:
                                    print("""
                            ****************Invalid email address,please try again2****************
                            """)
                                    print()
                                    print()
                                    print()
                                    print('''
                                                             PRESS 1: FOR BACK
                                                             PRESS 2: FOR EXIT
                                                             PRESS 3: FOR CONTINUE''')
                                    p1=int(input("ENTER YOUR INPUT: "))
                                    if p1==1:
                                        from admin import user
                                        user()
                                    if p1==2:
                                        exit()
                            break
                    except Exception as e:
                            print(str(e))
            
            elif press==2:
                print()
                print()
                user_create_account()
                break
            elif press==3:
                from log_in import log_in
                log_in()
            elif press==4:
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

#user()