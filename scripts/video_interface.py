import sqlite3

def search_videos(criteria):
    # Connect to the SQLite database
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()

    # Execute SQL query based on search criteria
    cursor.execute('''SELECT * FROM Videos WHERE category=? OR tags LIKE ? OR timestamp=?''', criteria)
    videos = cursor.fetchall()

    # Close the connection
    conn.close()

    return videos

def display_search_results(videos):
    # Display search results in a visually appealing manner
    print("Search Results:")
    print("--------------------------------------------------------")
    print("{:<10} | {:<20} | {:<30} | {:<20} | {:<20}".format("Video ID", "Title", "Category", "Tags", "Timestamp"))
    print("--------------------------------------------------------")
    
    for video in videos:
        video_id, title, category, tags, timestamp, _ = video  # Extract video information
        # Customize the display format as per your requirements
        print("{:<10} | {:<20} | {:<30} | {:<20} | {:<20}".format(video_id, title[:20], category, tags[:30], timestamp))
    
    print("--------------------------------------------------------")

if __name__ == "__main__":
    # Example usage: Search for videos based on criteria and display the results
    search_criteria = ('social media', '%funny%', '2022-01-01')  # Example criteria (replace with actual criteria)
    search_results = search_videos(search_criteria)
    display_search_results(search_results)


if __name__ == "__main__":
    # usage: Search for videos based on criteria and display the results
    search_criteria = ('social media', '%funny%', '2022-01-01')  #  criteria (replace with actual criteria)
    search_results = search_videos(search_criteria)
    display_search_results(search_results)