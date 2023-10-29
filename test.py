i=0
                                    id=int(input("ENTER  ID NUMBER: "))
                                    f1=f"select id from user where id={id}"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        for r2 in r1:
                                            if r2==id:
                                                i+=1
                                    e=input("enter your email: ")
                                    f1=f"select email from user where email='{e}'"
                                    s.execute(f1)
                                    r=s.fetchall()
                                    for r1 in r:
                                        for r2 in r1:
                                            if e in r2:
                                                i+=1
                                    if i==2:
                                        break