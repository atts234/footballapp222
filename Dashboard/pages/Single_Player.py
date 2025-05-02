import streamlit as st
import pandas as pd

def app():
    df = pd.read_csv("df_forwards.csv")
    top_features = ['Shots', 'Minutes Played', 'Big chances missed', 'Matches Played',
                    'Shooting accuracy %', 'Freekicks scored', 'Days Missed', 'Performance']

    st.header("👤 Single Player Performance View")
    st.markdown("Select a forward to view their metrics and predicted performance rating.")

    player = st.selectbox("Select a Forward", df["Player"].unique())
    player_data = df[df["Player"] == player][top_features]

    if not player_data.empty:
        st.subheader(f"Player: {player}")
        st.dataframe(player_data.drop(columns=["Performance"]))
        st.success(f"🏅 Predicted Performance: **{player_data['Performance'].values[0]}**")
