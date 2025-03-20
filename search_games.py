import sqlite3

def search_games(keyword):
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    
    # 検索クエリ
    query = "SELECT title, release_date, platform, category FROM games WHERE title LIKE ?"
    cursor.execute(query, ('%' + keyword + '%',))
    
    # 結果を取得
    results = cursor.fetchall()
    conn.close()
    
    return results

# テスト（"マリオ" を検索）
if __name__ == "__main__":
    keyword = input("検索するゲーム名: ")
    results = search_games(keyword)

    print("\n検索結果:")
    for game in results:
        print(game)
