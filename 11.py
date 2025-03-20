import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# push_history のデータを確認
cursor.execute("SELECT * FROM push_history LIMIT 10")
rows = cursor.fetchall()

print("push_history のデータ:")
for row in rows:
    print(row)

conn.close()
