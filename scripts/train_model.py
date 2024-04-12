import sys
import numpy as np 
sys.path.append('') #Add path to the clone root folder
from models.generative_ai_model import create_generative_ai_model
from scripts.preprocess_data import preprocess_video_data

def train_model(training_data, training_labels):
    # Create and compile the model
    model = create_generative_ai_model()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Preprocess the training data
    preprocessed_data = preprocess_video_data(training_data)

    # Train the model
    model.fit(preprocessed_data, training_labels, epochs=10, batch_size=32)

    #Save the model
    model.save("generative_ai_model_weights.h5")

def load_training_data():
    # if your training data is stored in a file named "training_data.npy":
    training_data = np.load("training_data.npy")
    return training_data

def load_training_labels():
    training_labels = np.load("training_labels.npy")
    return training_labels

if __name__ == "__main__":
    # Replace with actual training data and labels
    training_data = load_training_data()  
    training_labels = load_training_labels() 
    train_model(training_data, training_labels)
