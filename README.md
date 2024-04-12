# Video Curation AI

## Introduction
VisualTech Innovations is developing a groundbreaking Video Curation AI project aimed at organizing and categorizing unstructured video data into a structured and searchable database. This visionary initiative tackles the formidable challenges posed by the ever-growing volumes of video content from diverse sources such as social media, digital archives, and surveillance feeds.

## Methodologies
- **Generative AI Model**: Embarked on the pioneering development of a Generative AI model utilizing cutting-edge TensorFlow/Keras technology. This powerful model intelligently analyzes video data, discerning subjects, themes, and contexts, and categorizes them with remarkable accuracy.
- **Data Preprocessing**: Implemented a meticulously crafted suite of data preprocessing techniques to meticulously prepare video data for model input. This comprehensive process includes the precise resizing of frames and the normalization of pixel values, ensuring optimal performance.
- **Database Integration**: Seamlessly integrated the AI model with a sophisticated SQLite database system. This robust integration allows for the seamless storage of video metadata and predictions, facilitating efficient retrieval and organization of video content.
- **User Interface**: Pioneered the design of an innovative web interface using the Flask framework. This user-friendly interface provides intuitive querying and display capabilities, empowering users to effortlessly explore the curated video database.

## Challenges Encountered
1. **Data Preprocessing**: Navigating the complexities of ensuring consistency in frame sizes and pixel values across an array of disparate video sources.
2. **Model Training**: Tackling the formidable task of optimizing model architecture and hyperparameters to achieve precise categorization of diverse video content.
3. **Database Integration**: Confronting the challenge of managing and processing vast volumes of video data while maintaining optimal storage and retrieval efficiency.
4. **User Interface Design**: Striking the delicate balance between functionality and simplicity, ensuring that the web interface remains intuitive and user-friendly.

## Solutions Applied
1. **Data Preprocessing**: Implemented robust resizing and normalization techniques leveraging state-of-the-art OpenCV technology. These advanced techniques ensure uniformity in preprocessed video data, enhancing model performance.
2. **Model Training**: Undertook extensive experimentation with a myriad of model architectures and hyperparameters, leveraging transfer learning from pre-trained models to optimize performance.
3. **Database Integration**: Employed sophisticated batch processing and indexing strategies to optimize database performance, facilitating seamless handling of large datasets.
4. **User Interface Design**: Conducted iterative refinement of the web interface based on user feedback and rigorous usability testing. Prioritized key features while minimizing complexity, resulting in a streamlined and intuitive user experience.


# Running the Project

To run the project step by step, follow these instructions:

1. **Set Up the Environment**:
   - Ensure that Python is installed on your system.
   - Install the required packages by executing `pip install -r requirements.txt` in your terminal. Make sure you have a `requirements.txt` file containing the necessary dependencies.

2. **Prepare the Data**:
   - Place your video data files in the `data/` directory.

3. **Create the Database**:
   - Run `python scripts/create_database.py` in your terminal to create the SQLite database (`video_database.db`) and set up the necessary tables.

4. **Train the Generative AI Model**:
   - Execute `python scripts/train_model.py` in your terminal to train the Generative AI model using the provided training data.
   - This script will preprocess the training data, train the model, and save the trained model weights (`generative_ai_model_weights.h5`).

5. **Store Predictions in the Database**:
   - Run `python scripts/store_predictions_in_database.py` in your terminal to run the trained model on video data and store the predictions in the database.
   - The script will load the trained model, preprocess the video data, predict categories and tags, and update the database with the predictions.

6. **Run the Flask Application**:
   - Start the Flask application by running `python app.py` in your terminal.
   - This action will launch the web interface, allowing users to query and display videos from the database.
   - Access the interface by navigating to `http://localhost:5000` in your web browser.

7. **Explore the Results**:
   - Utilize the search functionality provided by the Flask application to explore the curated video database based on various criteria.
   - View the results in the web interface (`templates/results.html`).

Following these step-by-step instructions should assist you in running the project smoothly. Adjust the required areas for the file as per requirement.