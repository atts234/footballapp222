import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.header("📊 Team-Level Aggregated Stats (Forwards Only)")

    # Load data
    df = pd.read_csv("team_aggregates.csv")

    # Define relevant forward-specific metrics
    forward_metrics = [
        'Team', 
        'Total Minutes Played', 
        'Total Games Missed', 
        'Total Days Missed',
        'Average Shooting Accuracy %',
        'Total Big Chances Missed'
    ]

    df = df[forward_metrics]

    # User selects metric
    metric = st.selectbox("Select a metric to visualize:", forward_metrics[1:])

    # Sort by selected metric (descending)
    df_sorted = df.sort_values(by=metric, ascending=False)

    # Bar chart
    st.subheader("Bar Chart")
    fig, ax = plt.subplots()
    ax.barh(df_sorted['Team'], df_sorted[metric], color='steelblue')
    ax.set_xlabel(metric)
    ax.set_ylabel("Team")
    ax.invert_yaxis()
    st.pyplot(fig)

    # Table
    st.subheader("Sorted Team Statistics Table")
    st.dataframe(df_sorted.reset_index(drop=True))



