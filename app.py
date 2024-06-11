import streamlit as st
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import pickle
import os
import numpy as np

model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

feature_list = pickle.load(open('features.pkl', 'rb'))
filenames = pickle.load(open('filenames.pkl', 'rb'))

def save_uploaded_image(uploaded_image):
    try:
        with open(os.path.join('uploads', uploaded_image.name), 'wb') as f:
            f.write(uploaded_image.getbuffer())
        return True
    except:
        return False

def feature_extractor(img_path,model):
    img = image.load_img(img_path,target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img = np.expand_dims(img_array,axis=0)
    preprocessed_img = preprocess_input(expanded_img)
    result = model.predict(preprocessed_img).flatten()
    return result

st.title('Which Bollywood Celebrity Are You?')

uploaded_image = st.file_uploader('Choose an image')

if uploaded_image is not None:
    if save_uploaded_image(uploaded_image):
        display_image = Image.open(uploaded_image)

        img_path = os.path.join('uploads', uploaded_image.name)
        uploaded_features = feature_extractor(img_path, model)

        if uploaded_features is not None:
            similarity_scores = cosine_similarity([uploaded_features], feature_list)
            index_pos = np.argmax(similarity_scores)
            predicted_actor = " ".join(filenames[index_pos].split('\\')[1].split('_'))

            col1, col2 = st.columns(2)
            with col1:
                st.header('Your Uploaded Image')
                st.image(display_image)
            with col2:
                st.header("Seems like " + predicted_actor)
                st.image(filenames[index_pos], width=300)
        else:
            st.error('No face detected. Please upload a different image.')
