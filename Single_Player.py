import streamlit as st
import pandas as pd

df = pd.read_csv("df_forwards.csv")

top_features = ['Age', 'Shots', 'Minutes Played', 'Big chances missed',
                'Matches Played', 'Shooting accuracy %', 'Freekicks scored', 'Days Missed']

st.title("📋 Single Player Performance")

player_name = st.selectbox("Select a Forward", df["Player"].unique())

player_data = df[df["Player"] == player_name][top_features + ["Performance"]]

if not player_data.empty:
    st.subheader(f"Player: {player_name}")
    st.dataframe(player_data[top_features])
    perf = player_data["Performance"].values[0]
    st.success(f"🏆 Predicted Performance: **{perf}**")
