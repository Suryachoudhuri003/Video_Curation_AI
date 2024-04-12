import sys
sys.path.append('') #Add path to the clone root folder
import sqlite3
import numpy as np
from models.generative_ai_model import create_generative_ai_model
from scripts.preprocess_data import preprocess_video_data

def store_predictions_in_database(video_data):
    # Connect to the SQLite database
    conn = sqlite3.connect('video_database.db')
    cursor = conn.cursor()

    # Load the trained AI model
    model = create_generative_ai_model()
    model.load_weights('generative_ai_model_weights.h5')  # Load the trained model weights

    # Preprocess the video data
    preprocessed_data = preprocess_video_data(video_data)

    # Iterate through each video
    for i, video in enumerate(video_data):
        # Run the model on the preprocessed video data to get predictions
        predictions = model.predict(np.expand_dims(preprocessed_data[i], axis=0))

        # Convert predictions to category and tags (replace this with your actual post-processing code)
        predicted_category = 'example_category'
        predicted_tags = 'example_tags'

        # Store the predictions in the database along with video metadata
        cursor.execute('''UPDATE Videos SET predicted_category=?, predicted_tags=? WHERE video_id=?''',
                       (predicted_category, predicted_tags, i+1))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Replace [...] with actual video data (numpy arrays or file paths)
    video_data = [...]  # Replace [...] with your actual video data
    store_predictions_in_database(video_data)
