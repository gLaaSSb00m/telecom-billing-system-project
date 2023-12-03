from database import *
import re
def user_create_account():
      while(True):
            try:
                  print('''
                        1- FOR BACK
                        2- FOR EXIT
                        3- FOR CONTINUE
            ''')
                  press=int(input("ENTER THE INPUT:   "))
                  if press==1:
                        from log_in import log_in
                        log_in()
                  if press ==2:
                        exit()
                  if press==3:
                        
                        def check_password(password):
                              if len(password) < 8:
                                    print("Password must be at least 8 character")
                                    return False

                  # Check if the password contains at least one uppercase letter
                              if not re.search(r"[A-Z]", password):
                                    print("Password must be at least 1 capital letter")
                                    return False

                  # Check if the password contains at least one lowercase letter
                              if not re.search(r"[a-z]", password):
                                    print("Password must be at least 1 small letter")
                                    return False

                  # Check if the password contains at least one digit
                              if not re.search(r"\d", password):
                                    print("Password must be at least 1 digit")
                                    return False

                  # Check if the password contains at least one special character
                              if not re.search(r"[!@#$%^&*()_+=\-[\]{};':\"\\|,.<>/?]", password):
                                    print("Password must be at least 1 special character")
                                    return False

                              return True
                        def check_nid(nid):
                              pattern=r'^\d{13}$'
                              if re.match(pattern,nid):
                                    s.execute("select nid from user(13 digit)")
                                    v=s.fetchall()
                                    for t in v:
                                          if nid in t:
                                                print("This nid has been used")
                                                return False
                                    return True
                              else:
                                    print("Invalid nid number")
                                    return False
                        def check_ac_name(ac_name):
                              pattern=r"(nagad|bkash|rocket)"
                              if re.search(pattern,ac_name,re.IGNORECASE):
                                    return True
                              else:
                                    print("Invalid account name")
                                    return False
                        def check_ac_number(ac_number):
                              pattern=r'^\d{11}$'
                              if re.match(pattern,ac_number):
                                    return True
                              else:
                                    print("Invalid acount number, Please try again")
                                    return False
                        def mobile_check(mobile):
                              pattern = r'^\d{11}$'
                              if re.match(pattern, mobile):
                                    s.execute("select telephone from user")
                                    v=s.fetchall()
                                    for t in v:
                                          if mobile in t:
                                                print("This telephone has been used")
                                                return False
                                    return True
                              else:
                                    print("Invalid phone number,please try again")
                                    return False

                        def check_name(name):
                              
                              if len(name)>=6:
                                    return True
                              else:
                                    print("Name at least 6 character")
                                    return False
                        def check_email(email):
                                    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                                    if re.match(pattern, email):
                                          s.execute("select email from user")
                                          value=s.fetchall()
                                          for t in value:
                                                if email in t:
                                                      print("this email adress has been used")
                                                      return False
                                          return True
                                    else:
                                          print("Invalid email adress")
                                          return False
                        while True:
                              name=input("Enter your user name: ")
                              if check_name(name):
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                  
                        while True:
                              user_email = input("Enter an email address: ")

                              if check_email(user_email):
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                        while True:
                              try:
                                    mobile=input("Enter your telephone number: ")
                                    if mobile_check(mobile):
                                          print("ok")
                                          break
                                    else:
                                          print()
                                          print()
                                          print()
                              except Exception as e:
                                    print("Please enter a Int number",str(e))
                        while True:
                              ac_number=input("Enter your account number: ")
                              if check_ac_number(ac_number):
                                    print("ok")
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                        while True:
                              ac_name=input("Enter your Accont name: ")
                              if check_ac_name(ac_name):
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                        while True:
                              nid=input("Enter your nid: ")
                              if check_nid(nid):
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                        while True:
                              password=input("Enter your Password: ")
                              if check_password(password):
                                    break
                              else:
                                    print()
                                    print()
                                    print()
                        while True:
                              con_pass=input("Enter your confirm password: ")
                              if con_pass==password:
                                    break
                              else:
                                    print("Did no match")
                                    print()
                                    print()
                                    print()


                                    
                        f="insert into user (name,password,email,telephone,account_number,account_name,nid) values(%s,%s,%s,%s,%s,%s,%s)"
                        user=(name,password,user_email,mobile,ac_number,ac_name,nid)
                        s.execute(f,user)
                        mydb.commit()
                        print('''
                              ACCOUNT CREATE SUCCESSFULL
                              THANKS FOR USING THIS PLATFROM



                        ''')
            except Exception as e:
                  print(str(e))