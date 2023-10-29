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
            """)
        
            press=int(input("Enter Your Input: "))
            if press==1:
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
                                    if check_password(entered_password):
                                        break
                                    else:
                                        print("Password must be at least 1 special character, 1 digit, 1 capital letter")

                                #end
                                s.execute("select password from user")
                                value=s.fetchall()
                                found=False
                                for t in value:
                                    if entered_password in t:
                                        found=True
                                        break
                                if found:
                                    user_panal(user_email)
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
                ****************Invalid email address,please try again1****************
                """)
                        
                            print()
                            print()
                            print()
                        
                        
                    else:
                        print("""
                ****************Invalid email address,please try again2****************
                """)
                        print()
                        print()
                        print()
                break
            elif press==2:
                print()
                print()
                user_create_account()
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
