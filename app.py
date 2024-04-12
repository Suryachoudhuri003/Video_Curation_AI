from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Define route for querying videos
@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query')
    
    # Connect to the SQLite database
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()
    
    # Execute SQL query to retrieve videos based on title or tags
    cursor.execute('''SELECT * FROM Videos WHERE title LIKE ? OR tags LIKE ?''', ('%' + query + '%', '%' + query + '%'))
    videos = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return render_template('results.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)