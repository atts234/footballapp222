import streamlit as st
import numpy as np
import joblib

def app():
    st.header("🧠 Predict Performance from Player Stats")

    # Load trained model and scaler
    model = joblib.load("model_rf.pkl")
    scaler = joblib.load("scaler.pkl")

    st.markdown("Enter player details below:")

    player_name = st.text_input("Player Name")

    # Input fields for features
    shots = st.number_input("Shots", min_value=0)
    minutes_played = st.number_input("Minutes Played", min_value=0)
    big_chances_missed = st.number_input("Big Chances Missed", min_value=0)
    matches_played = st.number_input("Matches Played", min_value=0)
    shooting_accuracy = st.number_input("Shooting Accuracy (%)", min_value=0.0, max_value=100.0)
    freekicks_scored = st.number_input("Freekicks Scored", min_value=0)
    days_missed = st.number_input("Days Missed", min_value=0)

    if st.button("Predict Performance"):
        input_data = np.array([[shots, minutes_played, big_chances_missed,
                                matches_played, shooting_accuracy, freekicks_scored,
                                days_missed]])

        # Scale input
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        label_map = {0: 'Bad', 1: 'Average', 2: 'Good'}
        predicted_label = label_map.get(prediction, "Unknown")

        st.markdown(f"### 📋 Player: **{player_name or 'Unnamed'}**")
        st.success(f"🏅 Predicted Performance: **{predicted_label}**")
