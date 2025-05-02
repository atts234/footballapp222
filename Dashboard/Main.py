import streamlit as st
import pages.compare as compare
import pages.Single_Player as single
import pages.Top_Ranked as ranked

# Set page layout config
st.set_page_config(page_title="Player Performance Insights", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox("Select View", [
    "Home", 
    "Compare Players", 
    "Single Player View", 
    "Top 10 Forwards"
])

# Home Page
if page == "Home":
    st.title("⚽ Football Player Performance Insights")
    st.markdown("""
        ## Welcome to the **Player Performance Dashboard**
        This dashboard is designed to support coaches, analysts, and sports scientists by offering 
        machine learning–driven insights into the performance of football forwards.

        Explore anonymized data from any league and gain a better understanding of:
        - Workload and playing time
        - Missed chances and shot accuracy
        - Projected performance levels

        ---
        **Use the sidebar to:**
        - 🔍 View a single player's profile and performance category
        - ⚔️ Compare two forwards side by side
        - 📊 View top 10 ranked forwards
    """)

# Compare View
elif page == "Compare Players":
    compare.app()

# Single Player View
elif page == "Single Player View":
    single.app()

# Top 10 Rankings
elif page == "Top 10 Forwards":
    ranked.app()
