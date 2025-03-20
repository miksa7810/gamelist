import sqlite3

# データベース接続
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# "games" テーブルが存在するか確認
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='games';")
table_exists = cursor.fetchone()

# 存在しない場合は作成
if not table_exists:
    cursor.execute("""
        CREATE TABLE games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            push_count INTEGER DEFAULT 0
        )
    """)
    print("新しく 'games' テーブルを作成しました！")

# "push_count" カラムが存在するか確認
cursor.execute("PRAGMA table_info(games);")
columns = [column[1] for column in cursor.fetchall()]

if "push_count" not in columns:
    cursor.execute("ALTER TABLE games ADD COLUMN push_count INTEGER DEFAULT 0")
    print("'push_count' カラムを追加しました！")

# 変更を保存
conn.commit()
conn.close()

print("データベースのセットアップが完了しました！")

import sqlite3
import pandas as pd

# CSVファイルからデータを読み込む
csv_file = "game_list.csv"  # CSVファイル名（実際のファイル名を確認してください）
df = pd.read_csv(csv_file, encoding="utf-8-sig")

# SQLiteに接続
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# ゲームデータを追加
for index, row in df.iterrows():
    cursor.execute("INSERT INTO games (title, release_date, platform, developer) VALUES (?, ?, ?, ?)", 
                   (row["タイトル"], row["発売日"], row["ハード"], row["販売"]))

conn.commit()
conn.close()

