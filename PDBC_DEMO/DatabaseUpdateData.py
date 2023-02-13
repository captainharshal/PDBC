import DatabaseConn as DbConn

conn = DbConn.getconnection("marksheetdb1")
   
csr=conn.cursor()

rn = input("Enter Roll No.:\n")
nm= input("Enter New Name:\n") 
ph_score = input("Enter New Physics Score:\n")
ch_score = input("Enter New chemitry Score:\n")
mth_score = input("Enter New Maths Score:\n")

upd_qry = "UPDATE marksheet2 set student_name=%s,physics_score=%s,chemistry_score=%s,maths_score=%s where roll_no=%s"

row = csr.execute(upd_qry,(nm,ph_score,ch_score,mth_score,rn))

conn.commit()

if row == 0:
    print("Roll No. does not exist. Please enter the correct roll no.")
else:
    print("{} row affected".format(row))

csr.close()
conn.close()