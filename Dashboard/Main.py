import streamlit as st
import pages.compare as compare
import pages.Single_Player as single
import pages.Top_Ranked as ranked
import pages.Team_stats as team
import pages.Performance_Predictor as predict  # 🔥 New import

# Set page layout and title
st.set_page_config(page_title="Player Performance Insights", layout="wide")

# Sidebar page selection
page = st.sidebar.selectbox("Select View", [
    "Home", 
    "Compare Players", 
    "Single Player View", 
    "Top 10 Forwards", 
    "Team Stats",
    "Performance Predictor"  # 🔥 New option
])

# Home Page
if page == "Home":
    st.title("⚽ Football Player Performance Insights")
    st.markdown("""
        ## Welcome to the **Player Performance Dashboard**
        This dashboard helps coaches, analysts, and sports scientists:
        
        - Understand player workload and contributions
        - Identify missed opportunities and trends
        - View ML-predicted performance categories

        ---
        **Use the sidebar to explore:**
        - 🔍 Individual player breakdowns
        - ⚔️ Head-to-head forward comparisons
        - 🏆 Top 10 ranked forwards
        - 📊 Aggregated team-level stats
        - 🔮 Predict new player performance
    """)

elif page == "Compare Players":
    compare.app()

elif page == "Single Player View":
    single.app()

elif page == "Top 10 Forwards":
    ranked.app()

elif page == "Team Stats":
    team.app()

elif page == "Performance Predictor":
    predict.app()  # 🔥 New route

