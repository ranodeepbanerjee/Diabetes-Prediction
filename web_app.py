import numpy as np

import pickle

import streamlit as st

from PIL import Image

import requests

# Loading the saved data

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Creating a function for prediction

def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:

        return 'The person is not diabetic'

    else:

        return 'The person is diabetic'

def main():

    # Giving a title and setting page width

    st.set_page_config(page_title='Diabetes Prediction Web App', layout='wide')

    st.title('Diabetes Prediction Web App')

    # Loading the image from URL

    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsuHwwPoOUBHTp_vqyJpo_ExPeGki19m7rKQ&usqp=CAU'  #URL

    image = Image.open(requests.get(image_url, stream=True).raw)

    st.image(image, use_column_width=True)

    # Creating a side-by-side layout using columns

    col1, col2 = st.columns(2)

    # Getting the input data from the user

    with col1:

        st.header('Enter Patient Information')

        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

        glucose = st.number_input('Glucose Level', min_value=0, step=1)

        blood_pressure = st.number_input('Blood Pressure value', min_value=0, step=1)

        skin_thickness = st.number_input('Skin Thickness value', min_value=0, step=1)

    with col2:

        insulin = st.number_input('Insulin Level', min_value=0, step=1)

        bmi = st.number_input('BMI value', min_value=0.0, step=0.1)

        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.1)

        age = st.number_input('Age of the Person', min_value=0, step=1)

    # Code for prediction

    diagnosis = ''

    # Creating a button for prediction

    if st.button('Diabetes Test Result'):

        diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness,

                                         insulin, bmi, diabetes_pedigree_function, age])

    # Displaying the result

    st.subheader('Diabetes Prediction Result:')

    result_container = st.empty()

    if diagnosis:

        result_container.success(diagnosis)

    # Custom styling

    st.markdown(

        """

        <style>

        .stButton button {

            padding: 0.8em 1.6em;

            font-size: 1.2em;

            background-color: #FF6B6B;

            color: white;

            border-radius: 0.5em;

            border: none;

            box-shadow: none;

            transition: all 0.3s ease;

        }

        .stButton button:hover {

            background-color: #E63946;

        }

        .stTextInput input {

            padding: 0.6em;

        }

        </style>

        """,

        unsafe_allow_html=True

    )

if __name__ == '__main__':

    main()



