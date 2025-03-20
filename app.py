from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"  # セッション管理用

# データベース接続関数
def get_db_connection():
    conn = sqlite3.connect("games.db")
    conn.row_factory = sqlite3.Row
    return conn

# ユーザーIDを生成（セッションごとに一意のIDを付与）
def get_user_id():
    if "user_id" not in session:
        user_ip = request.remote_addr  # クライアントのIPアドレス
        session["user_id"] = hashlib.sha256(user_ip.encode()).hexdigest()[:10]  # 10桁のハッシュID
    return session["user_id"]

# 🔹 メインページ（ゲーム一覧表示 + 検索機能）
@app.route("/")
def index():
    search_query = request.args.get("search", "")  # 検索ワード取得
    user_id = get_user_id()  # 現在のユーザーIDを取得
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        cursor.execute("""
            SELECT g.id, g.title, g.release_date, g.platform, g.developer, g.push_count,
                   (SELECT COUNT(*) FROM push_history WHERE game_id = g.id AND user_id = ?) AS pushed
            FROM games g
            WHERE g.title LIKE ?
        """, (user_id, '%' + search_query + '%'))
    else:
        cursor.execute("""
            SELECT g.id, g.title, g.release_date, g.platform, g.developer, g.push_count,
                   (SELECT COUNT(*) FROM push_history WHERE game_id = g.id AND user_id = ?) AS pushed
            FROM games g
        """, (user_id,))

    games = cursor.fetchall()
    conn.close()
    return render_template("index.html", games=games, search_query=search_query)

# 🔹 推し機能（推しの追加・解除）
@app.route("/push/<int:game_id>", methods=["POST"])
def push_game(game_id):
    user_id = get_user_id()
    conn = get_db_connection()
    cursor = conn.cursor()

    # 既に推し済みかチェック
    cursor.execute("SELECT COUNT(*) FROM push_history WHERE game_id = ? AND user_id = ?", (game_id, user_id))
    already_pushed = cursor.fetchone()[0] > 0

    if already_pushed:
        # 既に推し済みなら削除（解除）
        cursor.execute("DELETE FROM push_history WHERE game_id = ? AND user_id = ?", (game_id, user_id))
        cursor.execute("UPDATE games SET push_count = push_count - 1 WHERE id = ?", (game_id,))
    else:
        # 推しを追加
        cursor.execute("INSERT INTO push_history (game_id, user_id) VALUES (?, ?)", (game_id, user_id))
        cursor.execute("UPDATE games SET push_count = push_count + 1 WHERE id = ?", (game_id,))

    conn.commit()
    conn.close()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
