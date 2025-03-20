import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# 📌 `release_date` カラムを追加
cursor.execute("ALTER TABLE games ADD COLUMN release_date TEXT")

# 📌 `platform`（ハード）と `developer`（メーカー）カラムもない場合、追加
cursor.execute("ALTER TABLE games ADD COLUMN platform TEXT")
cursor.execute("ALTER TABLE games ADD COLUMN developer TEXT")

conn.commit()
conn.close()

print("✅ `release_date`, `platform`, `developer` カラムを追加しました！")
