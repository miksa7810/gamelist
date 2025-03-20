from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# データベース接続関数
def get_db_connection():
    conn = sqlite3.connect("games.db")
    conn.row_factory = sqlite3.Row  # データを辞書形式で取得
    return conn

# 🔹 ゲーム一覧ページ + 検索機能
@app.route("/")
def index():
    search_query = request.args.get("search", "")  # 検索ワード取得
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        cursor.execute("SELECT id, title, release_date, platform, push_count FROM games WHERE title LIKE ?", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT id, title, release_date, platform, push_count FROM games")

    games = cursor.fetchall()
    conn.close()
    return render_template("index.html", games=games, search_query=search_query)

# 🔹 推し機能（推し数を増やす）
@app.route("/push/<int:game_id>", methods=["POST"])
def push_game(game_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE games SET push_count = push_count + 1 WHERE id = ?", (game_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
