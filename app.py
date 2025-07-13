import streamlit as st
from model import make_prediction

st.set_page_config(
    page_title= "Predict Diabetes"
)



st.title('Diabetes prediction')
st.header('Input your Data:')


glucose = st.number_input('Glucose', min_value =0, max_value=400, value=100)
blood_pressure = st.number_input('Blood Pressure', 50,300,120)
dfp = st.number_input('DFP',0,10,0)
age = st.number_input('Age',20,80,40)

if st.button('Predict'):
    input = [glucose, blood_pressure, dfp, age]
    prediction = make_prediction(input)

    if prediction[0] == 1:
        st.warning('High probality of Diabetes')
        st.write('see your Doctor')

    else:
        st.success('Low Chance of Diabetes')