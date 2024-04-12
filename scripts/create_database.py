import sqlite3
import os

def populate_video_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()

    # Path to the data folder
    data_folder = r'D:\Desktop\project\data'

    # Retrieve list of video files from the data folder
    video_files = os.listdir(data_folder)

    # Insert records into the Videos table for each video file
    for video_file in video_files:
        # Extract metadata from the video file name (e.g., title, category, tags, timestamp)
        title = os.path.splitext(video_file)[0]  # Extract title from file name
        category = 'uncategorized'  # Set category for the video
        tags = 'tag1,tag2,tag3'  # Set tags for the video
        timestamp = 'YYYY-MM-DD HH:MM:SS'  # Set timestamp for the video
        file_path = os.path.join(data_folder, video_file)  # Set file path for the video

        # Insert record into the Videos table
        cursor.execute('''INSERT INTO Videos (title, category, tags, timestamp, file_path)
                          VALUES (?, ?, ?, ?, ?)''', (title, category, tags, timestamp, file_path))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_video_database()