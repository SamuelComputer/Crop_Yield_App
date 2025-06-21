# 🌾 Crop Yield Prediction Web Application

This project is a **Machine Learning-based Crop Yield Prediction Web Application**. It utilizes historical agricultural data to predict crop yields based on various environmental and farming features. The web interface is built using **Streamlit**, allowing users to easily interact with the model and make predictions.

---

## 📂 Dataset Information

**Dataset Source:** [Kaggle - Crop Yield Prediction Dataset](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset/data?select=yield_df.csv)

The dataset includes farm-level data featuring crop types, rainfall, temperature, pesticide usage, and other factors influencing crop yield.

### 🔑 Key Features

| Feature | Description |
|---------|-------------|
| **ID** | Unique identifier for each farm record |
| **Item** | Type of crop cultivated (e.g., Cotton, Carrot, Wheat) |
| **Average_Rainfall (mm/year)** | Average rainfall during cultivation |
| **Average_Temperature** | Average temperature during cultivation |
| **Year** | Year of cultivation |
| **Area** | Geographical area of cultivation |
| **Pesticide_Used (tons)** | Quantity of pesticide used |
| **Yield (hg/ha)** | Actual crop yield (Target variable) |

---

## 🎯 Project Objective

- Analyse the relationship between climatic, environmental, and farming variables and crop yields.
- Build predictive models capable of estimating crop yields from input features.
- Deploy a user-friendly web application for real-time crop yield predictions.

---

## 🧪 Machine Learning Workflow

1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical variables (`Item`, `Area`)
   - Feature scaling where necessary

2. **Model Development**
   - **Linear Regression** (baseline model)
   - **Random Forest Regressor** (final selected model)

3. **Model Evaluation**
   - Root Mean Squared Error (RMSE)
   - Mean Absolute Error (MAE)
   - R-squared (R²)

4. **Deployment**
   - Streamlit web application

---

## 🤖 Best Model Performance

The **Random Forest Regressor** outperformed other models based on evaluation metrics and was deployed for real-time predictions.

---

## 💻 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn

---

## 🌐 Web Application Features

- Interactive input fields for real-time predictions
- Model evaluation metrics display
- Simple, clean user interface using Streamlit

---

## Live Demo

You can try the live version of the application here: [Crop Yield Prediction App](https://croppy.streamlit.app/)

---
