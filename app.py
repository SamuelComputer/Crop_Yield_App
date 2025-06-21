import streamlit as st
import joblib
import pandas as pd

# Load model and encoder
model = joblib.load('crop_yield_model.pkl')
ohe = joblib.load('ohe_encoder.pkl')

# Get categories from encoder
area_categories = ohe.categories_[0]
item_categories = ohe.categories_[1]

# Streamlit interface
st.title("🌾 Crop Yield Prediction App")

st.header("Enter the details:")

area = st.selectbox("Select Area", area_categories)
item = st.selectbox("Select Crop Type", item_categories)
rainfall = st.number_input("Average Rainfall (mm)", min_value=0.0)
pesticides = st.number_input("Pesticides Used (tonnes)", min_value=0.0)
temp = st.number_input("Average Temperature (°C)", min_value=0.0)

if st.button("Predict"):

    # Create dataframe for input
    input_df = pd.DataFrame([{
        "Area": area,
        "Item": item,
        "pesticides_tonnes": pesticides,
        "avg_temp": temp,
        "average_rain_fall_mm_per_year": rainfall
    }])

    # Apply encoder
    encoded_cats = ohe.transform(input_df[["Area", "Item"]])

    # Combine encoded categorical and numerical features
    numerical_features = input_df[["pesticides_tonnes", "avg_temp", "average_rain_fall_mm_per_year"]].values
    final_input = pd.concat([
        pd.DataFrame(encoded_cats),
        pd.DataFrame(numerical_features)
    ], axis=1)

    # Predict
    predicted_yield = model.predict(final_input)[0]

    st.success(f"Predicted Crop Yield: {predicted_yield:.2f} hg/ha")

st.write("© 2025 Smart Agro ")

st.write("Contact me here, samuelsundayiyanu@gmail.com")
