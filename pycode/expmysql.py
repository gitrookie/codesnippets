import MySQLdb

db = MySQLdb.connect(host="localhost", user="debian-sys-maint",
                     passwd="d7tU2l2MBgleTFVo", db="mydb")
cursor = db.cursor()
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# for (table_name,) in cursor:
#     print(table_name)
cursor.execute("SELECT * FROM node_type")

# cursor.execute("DESCRIBE node")
rows = cursor.fetchall()
print(rows)
db.close()
