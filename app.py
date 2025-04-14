from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# データベース接続関数
def get_db_connection():
    conn = sqlite3.connect("games.db")
    conn.row_factory = sqlite3.Row
    return conn

# 🔹 メインページ（ゲーム一覧表示 + 検索機能）
@app.route("/")
def index():
    search_query = request.args.get("search", "")
    series_query = request.args.get("series", "")

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        SELECT id, title, release_date, platform, developer
        FROM games
        WHERE 1=1
    """
    params = []

    if search_query:
        sql += " AND title LIKE ?"
        params.append(f"%{search_query}%")

    if series_query:
        sql += " AND series LIKE ?"
        params.append(f"%{series_query}%")

    sql += " ORDER BY title LIMIT 100"

    cursor.execute(sql, params)
    games = cursor.fetchall()
    conn.close()

    return render_template("index.html", games=games, search_query=search_query, series_query=series_query)

if __name__ == "__main__":
    app.run(debug=True)
