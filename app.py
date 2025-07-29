import streamlit as st
from model import make_prediction

st.set_page_config(page_title="Predict Diabetes")

st.title('Diabetes prediction')
st.header('Input your Data:')

glucose = st.number_input('Glucose', min_value=0, max_value=400, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=300, value=120)
dfp = st.number_input('DFP', min_value=0, max_value=10, value=0)
age = st.number_input('Age', min_value=1, max_value=120, value=40)

if st.button('Predict'):
    features = [glucose, blood_pressure, dfp, age]
    try:
        prediction = make_prediction(features)
        if prediction[0] == 1:
            st.warning('High probability of Diabetes')
            st.write('Please consult your doctor.')
        else:
            st.success('Low Chance of Diabetes')
    except Exception as e:
        st.error(f"Prediction failed: {e}")