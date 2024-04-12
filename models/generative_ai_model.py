import tensorflow as tf
num_classes = 10  # Replace 10 with the actual number of classes in your dataset
# Define frame dimensions
frame_height = 224  # Chenge with actual Height of each frame as per requirememnt
frame_width = 224   # Change actual Width of each frame as per requirement
def create_generative_ai_model(num_classes):
    # Define the CNN layers for spatial feature extraction
    cnn_layers = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(frame_height, frame_width, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten()
    ])
    
    # Define the RNN layers for temporal modeling
    rnn_layers = tf.keras.Sequential([
        tf.keras.layers.LSTM(256)
    ])

    # Combine the CNN and RNN layers
    model = tf.keras.Sequential([
        tf.keras.layers.TimeDistributed(cnn_layers),
        tf.keras.layers.TimeDistributed(tf.keras.layers.Flatten()),
        rnn_layers,
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    return model