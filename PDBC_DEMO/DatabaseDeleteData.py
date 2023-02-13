import DatabaseConn as DbConn

conn = DbConn.getconnection("marksheetdb1")
   
csr=conn.cursor()

rn = input("Enter Roll No.:\n")

del_qry = "DELETE from marksheet2 where roll_no=%s"

row = csr.execute(del_qry,(rn))

conn.commit()

if row == 0:
    print("Roll No. does not exist. Please enter the correct roll no.")
else:
    print("{} row affected".format(row))

csr.close()
conn.close()