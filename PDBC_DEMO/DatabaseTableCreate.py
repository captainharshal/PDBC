import DatabaseConn as DbConn

conn = DbConn.getconnection("marksheetdb1")

csr = conn.cursor()

crt_qry = """CREATE TABLE marksheet2 (sid int primary key AUTO_INCREMENT, roll_no int unique, student_name varchar(20), 
          physics_score int, chemistry_score int, maths_score int)"""

csr.execute(crt_qry)

conn.commit()

print("Table Created Successfully")

csr.close()

conn.close()

