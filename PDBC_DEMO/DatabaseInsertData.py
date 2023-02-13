import DatabaseConn as DbConn

def nextrn():

    Roll_No = 0

    conn = DbConn.getconnection("marksheetdb1")
    csr = conn.cursor()

    slt_qry = "select max(roll_no) from marksheet2"
    
    csr.execute(slt_qry)
    Roll_No = csr.fetchone()

    if Roll_No[0] is None:
        new_rn = list(Roll_No)
        new_rn[0] = 0
        Roll_No = tuple(new_rn)
    return Roll_No[0]+1

    csr.close()
    conn.close()


rn = nextrn()
name= input("Enter Student Name:\n") 
ph_score = input("Enter Physics Score:\n")
ch_score = input("Enter chemitry Score:\n")
mth_score = input("Enter Maths Score:\n")

inst_qry = "INSERT INTO marksheet2 (roll_no,student_name,physics_score,chemistry_score,maths_score) values (%s,%s,%s,%s,%s)"

conn = DbConn.getconnection("marksheetdb1")

csr = conn.cursor()

row = csr.execute(inst_qry,(rn,name,ph_score,ch_score,mth_score))

conn.commit()

print("{} row affected".format(row))

csr.close()

conn.close()