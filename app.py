# Deployment Interface
import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('iris_model.pkl','rb'))

# Title
st.title('IRIS FLOWER CLASSIFICATION')

# Input from user
sepal_length = st.number_input('Sepal Length(cm)',min_value=4.0,max_value=8.0,step=0.1)
sepal_width = st.number_input('Sepal Width(cm)',min_value=2.0,max_value=5.0,step=0.1)
petal_length = st.number_input('Petal Length(cm)',min_value=1.0,max_value=7.0,step=0.1)
petal_width = st.number_input('Petal Width(cm)',min_value=0.1,max_value=3.0,step=0.1)

# Prediction Button
if st.button('Predict'):
    # Preparing Input
    features = np.array([[sepal_length,sepal_width,petal_length,petal_width]])
    # Make Prediction
    prediction = model.predict(features)

    # Map prediction to class label
    class_names = ['Setosa','Versicolor','Virginica']
    result = class_names[prediction[0]]
    st.success(f'Predicted Class: {result}')