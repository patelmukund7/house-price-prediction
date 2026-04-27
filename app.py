import streamlit as st
import pickle
import json
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Load column names
with open('columns.json', 'r') as f:
    columns = json.load(f)

st.title("House Price Prediction App")
# Numeric inputs
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=41)
total_rooms = st.number_input("Total Rooms", value=880)
total_bedrooms = st.number_input("Total Bedrooms", value=129)
population = st.number_input("Population", value=322)
households = st.number_input("Households", value=126)
median_income = st.number_input("Median Income", value=8.3252)


# Ocean proximity (categorical)
ocean = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "NEAR BAY", "NEAR OCEAN", "<1H OCEAN"]
)
if st.button("Predict Price"):

    # Create input array with zeros
    input_data = np.zeros(len(columns))

    # Fill numeric values
    input_dict = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income
    }

    for key in input_dict:
        if key in columns:
            index = columns.index(key)
            input_data[index] = input_dict[key]

    # Handle categorical (one-hot encoding)
    col_name = f"ocean_proximity_{ocean}"
    if col_name in columns:
        index = columns.index(col_name)
        input_data[index] = 1

    # Predict
    prediction = model.predict([input_data])[0]

    st.success(f"Estimated House Price: ${prediction:,.2f}")
