from database import *
def b_d(id):
    formula=f"select * from bill where id={id}"
    s.execute(formula)
    rs=s.fetchall()
    return rs