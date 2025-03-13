import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Placement Predictor (Beta)")

# Input fields
cgpa = st.number_input("Enter Student's CGPA:", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter Student's IQ:", min_value=50, max_value=200, step=1)

# Prediction button
if st.button("Predict"):
    # Ensure valid input
    if cgpa and iq:
        # Prepare input data
        input_data = np.array([[cgpa, iq]])
        prediction = model.predict(input_data)
        
        # Display result
        if prediction[0] == 1:
            st.success("Yes, you will be placed!")
        else:
            st.error("No, we are sorry.")
    else:
        st.warning("Please enter valid values for CGPA and IQ.")

# Beta disclaimer
st.markdown("**Note:** This is a beta version built on a very small dataset, hence the predictions may be incorrect.")

