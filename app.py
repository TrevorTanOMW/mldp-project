import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("luxuryCar_rf.pkl")

# Define column names (same as training)
columns = [
    'Year', 'Horsepower', 'Engine Cylinders', 'Number of Doors', 'Highway MPG', 'City MPG',
    'Make_Alfa Romeo', 'Make_Aston Martin', 'Make_Audi', 'Make_BMW', 'Make_Bentley', 'Make_Bugatti',
    'Make_Buick', 'Make_Cadillac', 'Make_Chevrolet', 'Make_Chrysler', 'Make_Dodge', 'Make_FIAT',
    'Make_Ferrari', 'Make_Ford', 'Make_GMC', 'Make_Genesis', 'Make_HUMMER', 'Make_Honda',
    'Make_Hyundai', 'Make_Infiniti', 'Make_Kia', 'Make_Lamborghini', 'Make_Land Rover', 'Make_Lexus',
    'Make_Lincoln', 'Make_Lotus', 'Make_Maserati', 'Make_Maybach', 'Make_Mazda', 'Make_McLaren',
    'Make_Mercedes-Benz', 'Make_Mitsubishi', 'Make_Nissan', 'Make_Oldsmobile', 'Make_Plymouth',
    'Make_Pontiac', 'Make_Porsche', 'Make_Rolls-Royce', 'Make_Saab', 'Make_Scion', 'Make_Spyker',
    'Make_Subaru', 'Make_Suzuki', 'Make_Toyota', 'Make_Volkswagen', 'Make_Volvo',
    'Engine Fuel Type_electric', 'Engine Fuel Type_flex-fuel (unleaded/E85)', 'Engine Fuel Type_natural gas',
    'Engine Fuel Type_premium unleaded (recommended)', 'Engine Fuel Type_premium unleaded (required)',
    'Engine Fuel Type_regular unleaded',
    'Transmission Type_AUTOMATIC', 'Transmission Type_DIRECT_DRIVE', 'Transmission Type_MANUAL',
    'Transmission Type_UNKNOWN',
    'Driven Wheels_four wheel drive', 'Driven Wheels_front wheel drive', 'Driven Wheels_rear wheel drive',
    'Vehicle Size_Large', 'Vehicle Size_Midsize',
    'Vehicle Style_Coupe', 'Vehicle Style_Hatchback', 'Vehicle Style_Pickup', 'Vehicle Style_SUV',
    'Vehicle Style_Sedan', 'Vehicle Style_Van', 'Vehicle Style_Wagon',
    'Market Category Simplified_crossover', 'Market Category Simplified_diesel',
    'Market Category Simplified_green', 'Market Category Simplified_luxury',
    'Market Category Simplified_performance'
]

# UI
st.title("🚗 Luxury Car Price Predictor")

st.markdown("Fill in the details of the car below to predict its MSRP.")

# Inputs
year = st.number_input("Year", value=2021, min_value=1990, max_value=2025)
horsepower = st.number_input("Horsepower", value=542)
engine_cylinders = st.number_input("Engine Cylinders", value=8)
num_doors = st.selectbox("Number of Doors", [2, 4])
highway_mpg = st.number_input("Highway MPG", value=24)
city_mpg = st.number_input("City MPG", value=15)

make = st.selectbox("Make", ["Bentley", "Ferrari", "Porsche"])
fuel_type = st.selectbox("Fuel Type", ["premium unleaded (required)"])
transmission = st.selectbox("Transmission", ["AUTOMATIC"])
driven_wheels = st.selectbox("Driven Wheels", ["four wheel drive"])
vehicle_size = st.selectbox("Vehicle Size", ["Midsize"])
vehicle_style = st.selectbox("Vehicle Style", ["Coupe"])

luxury = st.checkbox("Luxury Category", value=True)
performance = st.checkbox("Performance Category", value=True)

# Predict button
if st.button("Predict MSRP"):
    # Create input template
    input_data = {col: 0 for col in columns}
    input_data.update({
        'Year': year,
        'Horsepower': horsepower,
        'Engine Cylinders': engine_cylinders,
        'Number of Doors': num_doors,
        'Highway MPG': highway_mpg,
        'City MPG': city_mpg,
        f'Make_{make}': 1,
        f'Engine Fuel Type_{fuel_type}': 1,
        f'Transmission Type_{transmission}': 1,
        f'Driven Wheels_{driven_wheels}': 1,
        f'Vehicle Size_{vehicle_size}': 1,
        f'Vehicle Style_{vehicle_style}': 1,
    })

    if luxury:
        input_data['Market Category Simplified_luxury'] = 1
    if performance:
        input_data['Market Category Simplified_performance'] = 1

    # Predict
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Predicted MSRP: **${prediction:,.2f}**")

