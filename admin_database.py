from database import *
def u_id(id):
    formula=f"select email,nid,telephone from user where id={id}"
    s.execute(formula)
    rs=s.fetchall()
    return rs
def u_email(id):
    formula=f"select id,nid,telephone from user where id={id}"
    s.execute(formula)
    rs=s.fetchall()
    return rs
def u_telephone(id):
    formula=f"select id,nid,email from user where id={id}"
    s.execute(formula)
    rs=s.fetchall()
    return rs