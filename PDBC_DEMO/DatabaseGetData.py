import DatabaseConn as DbConn

conn = DbConn.getconnection("marksheetdb1")
   
csr = conn.cursor()

slt_qry = "select * from marksheet2"

csr.execute(slt_qry)

# To fetch all records from Table as a nested tuple
Result = csr.fetchall()

print (Result)

for row in Result:
    print("{}\t{}\t{}\t\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))


# To fetch specified number of records from Table as a nested tuple
Result1 = csr.fetchmany(2)

print (Result1)

for row in Result1:
    print("{}\t{}\t{}\t\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))


# To fetch single top record from Table as a single tuple
Result2 = csr.fetchone()

print (Result2)
print("{}\t{}\t{}\t\t{}\t{}\t{}".format(Result2[0],Result2[1],Result2[2],Result2[3],Result2[4],Result2[5]))


csr.close()
conn.close()
