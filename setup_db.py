import sqlite3

# データベース接続
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# ゲームテーブルの作成（既に作成済みならスキップ）
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_date TEXT,
    platform TEXT,
    developer TEXT,
    push_count INTEGER DEFAULT 0
)
""")

# 🔹 `push_history` テーブルの作成
cursor.execute("""
CREATE TABLE IF NOT EXISTS push_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,  -- 🔹 ユーザーごとの推し管理用
    FOREIGN KEY (game_id) REFERENCES games (id)
)
""")

conn.commit()
conn.close()

print("データベースをセットアップしました。")
