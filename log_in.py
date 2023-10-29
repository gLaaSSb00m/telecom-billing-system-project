from admin import admin
from user import user
def log_in():
    while True:
        try:
            print("""
            -----------------------LOG IN---------------------
            ..................................................
            .                1. ADMIN_LOG_IN                 .
            ..................................................
            .                2. USER_LOG_IN                  .
            ..................................................
            """)
            press=int(input("Enter your input: "))
            if press==1:
                admin()
            elif press==2:
                user()
            else:
                print("invalid input, please try again")
                print()
                print()
        except Exception as e:
            print("sorry please enter a int number",str(e))
            print()
            print()
            print()