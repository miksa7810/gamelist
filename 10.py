import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("テーブル一覧:", tables)

conn.close()
