import sqlite3

# データベースに接続
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# `user_id` カラムが存在しない場合、追加
try:
    cursor.execute("ALTER TABLE push_history ADD COLUMN user_id TEXT")
    conn.commit()
    print("✅ `user_id` カラムを `push_history` テーブルに追加しました。")
except sqlite3.OperationalError:
    print("⚠️ `user_id` カラムはすでに存在しています。")

# 接続を閉じる
conn.close()
