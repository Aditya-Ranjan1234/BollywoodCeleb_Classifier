# Bollywood Celebrity Classifier

This project is a Bollywood Celebrity Classifier that uses a pre-trained VGG16 model to identify which Bollywood celebrity an uploaded image resembles. 

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Feature Extraction](#feature-extraction)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Introduction

The Bollywood Celebrity Classifier is built using a Convolutional Neural Network (CNN) based on the VGG16 architecture. It takes an image as input and predicts the Bollywood celebrity that the image resembles the most.

## Features

- **Image Upload**: Upload an image to the web app.
- **Feature Extraction**: Extract features from the uploaded image using VGG16.
- **Similarity Measurement**: Measure the cosine similarity between the uploaded image and a set of precomputed celebrity images.
- **Prediction**: Display the most similar celebrity image and name.

## Dataset

The dataset consists of images of various Bollywood celebrities. The images are used to extract features and build a similarity-based classifier. \
Link : https://www.kaggle.com/datasets/sushilyadav1998/bollywood-celeb-localized-face-dataset

## Model

The project uses the VGG16 model pre-trained on the ImageNet dataset. The top layers of the VGG16 model are removed, and the remaining layers are used to extract features from the images.

## Feature Extraction

The `feature_extractor` function extracts features from an image using the VGG16 model. The features are flattened and used to compute similarity with precomputed features of celebrity images.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Aditya-Ranjan1234/BollywoodCeleb_Classifier.git
    cd BollywoodCeleb_Classifier
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Download the pre-trained VGG16 model weights:**
    The weights are automatically downloaded when running the app for the first time.

## Usage

**IMP : First run featureExtractor.ipynb to get features.pkl**

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

2. **Upload an image:**
    - Go to the web browser where the Streamlit app is running.
    - Upload an image of a face.

3. **View the results:**
    - The app will display the uploaded image and the most similar Bollywood celebrity image along with the predicted name.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
