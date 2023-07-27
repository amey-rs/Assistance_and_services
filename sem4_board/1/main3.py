import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("datafile (1).csv")

# Rename column
df = df.rename(columns={"Yield (Quintal/ Hectare)": "Yield"})

# Define the app
def app():
    # Set the app title
    st.title("Crop Data Visualization App")

    # Add a sidebar
    st.sidebar.title("Visualization Settings")

    # Allow the user to select X and Y axes
    x_axis = st.sidebar.selectbox("X-Axis", list(df.columns), index=0)
    y_axis = st.sidebar.selectbox("Y-Axis", list(df.columns), index=5)

    # Allow the user to select a chart type
    chart_type = st.sidebar.selectbox("Chart Type", ["scatter", "line", "bar", "area", "box", "violin"])

    # Create the chart
    st.subheader(f"{chart_type.title()} Chart")
    if chart_type == "scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis, color="Crop")
    elif chart_type == "line":
        fig = px.line(df, x=x_axis, y=y_axis, color="Crop")
    elif chart_type == "bar":
        fig = px.bar(df, x=x_axis, y=y_axis, color="Crop")
    elif chart_type == "area":
        fig = px.area(df, x=x_axis, y=y_axis, color="Crop")
    elif chart_type == "box":
        fig = px.box(df, x="Crop", y=y_axis)
    elif chart_type == "violin":
        fig = px.violin(df, x="Crop", y=y_axis)

    # Display the chart
    if chart_type == "box" or chart_type == "violin":
        st.plotly_chart(fig)
    else:
        st.plotly_chart(fig, use_container_width=True)

    # Display a table of the data
    st.subheader("Data Table")
    st.write(df)

    # Allow the user to download the data
    csv = df.to_csv(index=False)
    st.download_button(
        "Download CSV",
        data=csv,
        file_name="crop_data.csv",
        mime="text/csv",
    )

# Run the app
if __name__ == "__main__":
    app()
