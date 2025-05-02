import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("df_forwards.csv")
df_forwards = df[df['Position'].str.contains('Forward', na=False)]

# Features to show
top_features = [
    'Shots','Minutes Played','Big chances missed','Matches Played',
    'Shooting accuracy %','Freekicks scored','Days Missed'
]
display_features = ['Age'] + top_features

# -- Page Config --
st.set_page_config(page_title="Premier League Player Dashboard", layout="wide")

# -- Custom CSS --
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .player-box {
        padding: 1.2rem;
        background-color: white;
        border-radius: 0.75rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }
    .stSelectbox > div {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# -- Title Section --
st.title("⚽ Premier League Performance Dashboard")
st.write("Compare anonymized forward player statistics and their predicted performance.")

# -- Sidebar Selections --
st.sidebar.title("🔎 Compare Two Forwards")
player1 = st.sidebar.selectbox("Select Player A", df_forwards["Player"].unique(), key="player1")
player2 = st.sidebar.selectbox("Select Player B", df_forwards["Player"].unique(), key="player2")

# -- Display Player Stats Side-by-Side --
col1, col2 = st.columns(2)

def show_player_card(player_name, color):
    player_data = df_forwards[df_forwards["Player"] == player_name]
    if not player_data.empty:
        st.markdown(f"<div class='player-box'>", unsafe_allow_html=True)
        st.subheader(f"🧍 {player_name}")
        st.dataframe(player_data[display_features], use_container_width=True)
        perf = player_data["Performance"].values[0]
        st.success(f"🏅 Predicted Performance: **{perf}**", icon="📊")
        st.markdown("</div>", unsafe_allow_html=True)

with col1:
    show_player_card(player1, "blue")

with col2:
    show_player_card(player2, "green")
