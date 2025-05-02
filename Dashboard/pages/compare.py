import streamlit as st
import pandas as pd

def app():
    df = pd.read_csv("df_forwards.csv")
    top_features = ['Shots', 'Minutes Played', 'Big chances missed', 'Matches Played',
                    'Shooting accuracy %', 'Freekicks scored', 'Days Missed', 'Performance']

    st.header("⚔️ Compare Two Forward Players")
    st.markdown("Select any two players below to compare their key performance metrics:")

    player1 = st.selectbox("Select Forward 1", df["Player"].unique())
    player2 = st.selectbox("Select Forward 2", df["Player"].unique())

    col1, col2 = st.columns(2)

    def show_player(player, col):
        data = df[df["Player"] == player][top_features]
        with col:
            st.subheader(f"👤 {player}")
            st.dataframe(data.drop(columns=["Performance"]))
            st.success(f"🏅 Predicted Performance: **{data['Performance'].values[0]}**")

    show_player(player1, col1)
    show_player(player2, col2)

