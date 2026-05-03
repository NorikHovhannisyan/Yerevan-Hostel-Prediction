import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json 

with open('hotel_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
    
with open('model_columns.json', 'r') as file:
    model_columns = json.load(file)
    
    
    
st.title('🏨Yerevan Hotel Price Prediction')
st.write('Enter hotel details and see an approximate price')

stars = st.slider('Count of Stars', 0, 5, 3)
rating = st.number_input('Overall rating (1-10)', 1.0, 10.0, 8.5)
cleanliness = st.number_input('Cleanliness (1-10)', 1.0, 10.0, 9.0)
comfort = st.number_input('Comfort (1-10)', 1.0, 10.0, 8.0)
facilities = st.number_input('Facilities (1-10)', 1.0, 10.0, 8.0)


if st.button('Calculate Price'):
    input_df = pd.DataFrame(0, index = [0], columns = model_columns)
    input_df.at[0, 'Star Rating'] = stars
    input_df.at[0, 'Rating'] = rating
    input_df.at[0, 'Cleanliness'] = cleanliness
    input_df.at[0, 'Comfort'] = comfort
    input_df.at[0, 'Facilities'] = facilities
    
    features_scaled = scaler.transform(input_df)
    prediction = model.predict(features_scaled)
    st.success(f"📈 Approximate hotel price per day: ${prediction[0]:.2f}")