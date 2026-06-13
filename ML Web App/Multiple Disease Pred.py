# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 08:27:49 2026

@author: karti
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the save models
diabetes_model = pickle.load(open('saved models/diabetes_model.sav', 'rb'))
scaler = pickle.load(open('saved models/scaler.sav', 'rb'))

heart_disease_model = pickle.load(open('saved models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('saved models/parkinsons_model.sav', 'rb'))
parkinsons_scaler = pickle.load(open('saved models/parkinsons_scaler.sav', 'rb'))

# sidebar for navigate
with st.sidebar:
    
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons = ['activity','heart','person'],
        default_index=0
    )
    
# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # First Row
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    # Second Row
    col4, col5, col6 = st.columns(3)

    with col4:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col5:
        Insulin = st.text_input("Insulin Level")

    with col6:
        BMI = st.text_input("BMI Value")

    # Third Row
    col7, col8, col9 = st.columns(3)

    with col7:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    with col8:
        Age = st.text_input("Age")

    # Leave the third column empty or add another widget
    with col9:
        st.empty()

    # code for Prediction
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        try:
            # Create input data
            input_data = [[
                int(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                int(Age)
            ]]

            # Apply StandardScaler
            input_data = scaler.transform(input_data)

            # Predict
            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        except ValueError: 
           diab_diagnosis = 'Please enter valid numeric values in all fields.'

    st.success(diab_diagnosis)
    
# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # Create 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain Types')

    # Second Row
    col4, col5, col6 = st.columns(3)

    with col4:
        trestbps = st.text_input('Resting Blood Pressure')

    with col5:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col6:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    # Third Row
    col7, col8, col9 = st.columns(3)

    with col7:
        restecg = st.text_input('Resting Electrocardiographic Results')

    with col8:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col9:
        exang = st.text_input('Exercise Induced Angina')

    # Fourth Row
    col10, col11, col12 = st.columns(3)

    with col10:
        oldpeak = st.text_input('ST Depression induced by Exercise')

    with col11:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')

    with col12:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy')

    # Fifth Row
    col13, col14 = st.columns(2)

    with col13:
        thal = st.text_input('Thal')
    
    with col14:
        st.empty()

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):

        try:
            heart_prediction = heart_disease_model.predict([[
                int(age),
                int(sex),
                int(cp),
                int(trestbps),
                int(chol),
                int(fbs),
                int(restecg),
                int(thalach),
                int(exang),
                float(oldpeak),
                int(slope),
                int(ca),
                int(thal)
            ]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having Heart Disease'
            else:
                heart_diagnosis = 'The person does not have any Heart Disease'

        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values in all fields.'

    st.success(heart_diagnosis)
    
# Parkinsons Prediction Page
if(selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction using ML')
    
    # input fields
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')


    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
       rap = st.text_input('MDVP:RAP')

    with col7:
        ppq = st.text_input('MDVP:PPQ')

    with col8:
        ddp = st.text_input('Jitter:DDP')

    with col9:
        shimmer = st.text_input('MDVP:Shimmer')

    with col10:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')


    col11, col12, col13, col14, col15 = st.columns(5)

    with col11:
        apq3 = st.text_input('Shimmer:APQ3')

    with col12:
        apq5 = st.text_input('Shimmer:APQ5')

    with col13:
        apq = st.text_input('MDVP:APQ')

    with col14:
        dda = st.text_input('Shimmer:DDA')

    with col15:
        nhr = st.text_input('NHR')


    col16, col17, col18, col19 = st.columns(4)

    with col16:
        hnr = st.text_input('HNR')

    with col17:
        rpde = st.text_input('RPDE')

    with col18:
        dfa = st.text_input('DFA')

    with col19:
        spread1 = st.text_input('Spread1')

 
    col20, col21, col22 = st.columns(3)
    
    with col20:
         spread2 = st.text_input('Spread2')

    with col21:
         d2 = st.text_input('D2')

    with col22:
         ppe = st.text_input('PPE')


   # Prediction

    parkinsons_diagnosis = ""

    if st.button("Parkinson's Test Result"):
        try:
            
            input_data = [[
                float(fo),
                float(fhi),
                float(flo),
                float(jitter_percent),
                float(jitter_abs),
                float(rap),
                float(ppq),
                float(ddp),
                float(shimmer),
                float(shimmer_db),
                float(apq3),
                float(apq5),
                float(apq),
                float(dda),
                float(nhr),
                float(hnr),
                float(rpde),
                float(dfa),
                float(spread1),
                float(spread2),
                float(d2),
                float(ppe)
           ]]

            # Apply StandardScaler
            input_data = parkinsons_scaler.transform(input_data)

            # Prediction

            prediction = parkinsons_model.predict(input_data)


            if prediction[0] == 1:
                 parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                 parkinsons_diagnosis = "The person does not have Parkinson's disease"

        except ValueError:
                parkinsons_diagnosis = "Please enter valid numeric values in all fields."

    st.success(parkinsons_diagnosis)

