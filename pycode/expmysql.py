import MySQLdb

db = MySQLdb.connect(host="localhost", user="debian-sys-maint",
                     passwd="d7tU2l2MBgleTFVo", db="mydb")
cursor = db.cursor()
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# print(tables)
# for (table_name,) in cursor:
#     print(table_name)
# cursor.execute("SELECT * FROM node_type")

# cursor.execute("DESCRIBE node")
# rows = cursor.fetchall()
# print(rows)

cursor.execute("select * from node_revisions")
rows = cursor.fetchall()
for row in rows:
    print(row)
    break

db.close()
