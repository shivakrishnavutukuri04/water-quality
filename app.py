import streamlit as st
import numpy as np
import pickle

# Load the trained SVM model
with open('svm_water_quality_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Water Quality Prediction')
st.write("Enter the water quality parameters to predict potability.")

# Input fields for user
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
Hardness = st.number_input("Hardness", min_value=0.0, value=100.0)
Solids = st.number_input("Solids (ppm)", min_value=0.0, value=20000.0)
Chloramines = st.number_input("Chloramines", min_value=0.0, value=5.0)
Sulfate = st.number_input("Sulfate", min_value=0.0, value=300.0)
Conductivity = st.number_input("Conductivity", min_value=0.0, value=500.0)
Organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
Trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=80.0)
Turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

# Predict button
if st.button("Predict Water Quality"):
    input_data = np.array([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    prediction = model.predict(input_data)
    result = "Safe to Drink" if prediction[0] == 1 else "Not Safe to Drink"
    st.write(f"Prediction: {result}")
