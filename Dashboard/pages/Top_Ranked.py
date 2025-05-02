import streamlit as st
import pandas as pd

def app():
    st.subheader("Top 10 Ranked Forwards")
    st.markdown("This list highlights the top 10 forwards based on their positional rank in the dataset.")

    # Load and filter top 10 players by positional rank
    df = pd.read_csv("df_forwards.csv")
    top10 = df.sort_values(by="Rank in Position").head(10)

    st.markdown("---")
    for i, row in top10.iterrows():
        with st.container():
            cols = st.columns([1, 6, 3])
            cols[0].markdown(f"### #{int(row['Rank in Position'])}")
            cols[1].markdown(f"**{row['Player']}**")
            cols[2].markdown(f"*{row['Team']}*")
        st.markdown("---")
