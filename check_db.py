import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# 📌 `games` テーブルのカラム一覧を取得
cursor.execute("PRAGMA table_info(games)")
columns = cursor.fetchall()

print("🎯 現在の `games` テーブルのカラム:")
for col in columns:
    print(col)

# 📌 `games` テーブルの最初の10件のデータを取得
cursor.execute("SELECT * FROM games LIMIT 10")
rows = cursor.fetchall()

print("\n📋 `games` テーブルの最初の10件:")
for row in rows:
    print(row)

conn.close()
