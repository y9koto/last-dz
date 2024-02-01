import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

print(connection)
print(cur)

connection.close()




#SELECT
cur.execute()
cur.execute("SELECT rowid, name FROM user")


