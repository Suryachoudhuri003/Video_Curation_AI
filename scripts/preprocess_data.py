import cv2
import numpy as np

def preprocess_video_data(video_data):
    # Initialize an empty list to store preprocessed frames
    preprocessed_data = []
    
    # Iterate through each frame in the video data
    for frame in video_data:
        # Resize each frame to a consistent size (e.g., 224x224)
        resized_frame = cv2.resize(frame, (224, 224))
        
        # Convert the frame to float32 and normalize pixel values to the range [0, 1]
        normalized_frame = resized_frame.astype(np.float32) / 255.0
        
        # Append the preprocessed frame to the list
        preprocessed_data.append(normalized_frame)
    
    # Convert the list of preprocessed frames to a numpy array
    preprocessed_data = np.array(preprocessed_data)
    
    return preprocessed_data

# Save training data and labels as numpy arrays
np.save("training.npy", preprocessed_data) # type: ignore

#For example, if your labels are stored in a CSV file named "labels.csv":
import pandas as pd
labels_df = pd.read_csv("labels.csv")
labels = labels_df['label'].tolist()
np.save("labels.npy", labels)

