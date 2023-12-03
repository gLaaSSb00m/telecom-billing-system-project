def name():
    print('''
                        
                        TELECOM BILLING SYSTEM
                        ......................
          
                TEAM MEMBERS       |   ID     
                                   |
                AL HOSSAIN ABID    |  21225103470
                AZAD HOSSAIN RAZU  |  21225103507
                TASNIM MAHMUD      |  21225103488
                PARVEZ HOSEN       |  21225103453
                MD. KHALID HASSSAN |  21225103492
                ---------------------------------
          
                    SUPERVISOR NAME:

                MD SADDAM HOSSAIN
                ASSISTANT PROFESSOR
                DEPARTMENT OF CSE
                BANGLADESH UNIVERSITY OF BUISNESS AND TECHNOLOGY
        

''')
    try:
        while(True):
            print(''''
                1: FOR CONTINUE
                0: FOR EXIT
                ''')
            p=int(input("ENTER YOUR INPUT: "))
            if p==1:
                from log_in import log_in
                log_in()
            elif p==0:
                exit()
            else:
                print("---------invalid input-------")
                print()
                print()

    except Exception as e:
        print(str(e))
#name()