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
import sqlite3

# データベースに接続
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# `push_history` テーブルのカラム情報を取得
cursor.execute("PRAGMA table_info(push_history)")
columns = cursor.fetchall()

# カラム情報を表示
print("push_history テーブルのカラム情報:")
for column in columns:
    print(column)

# 接続を閉じる
conn.close()
