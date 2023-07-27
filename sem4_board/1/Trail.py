import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Add a title and subtitle
st.title("Assistance and Trading Services")
st.subheader("Portal to generate the insight of the data for simplified understanding")

# Load the data from the CSV file
data = pd.read_csv("Kaggle.csv")

# Create a dropdown widget for selecting the commodity
commodity = st.selectbox("Select Commodity", data["commodity"].unique())

# Filter the data based on the selected commodity
filtered_data = data[data["commodity"] == commodity]

# Create a widget to display the modal price
st.write("Modal Price of", commodity)
st.write(filtered_data[["commodity", "modal_price"]].drop_duplicates())

# Create a sidebar widget for selecting the type of plot
plot_type = st.sidebar.selectbox("Select Type of Plot", ["Bar Plot", "Line Plot", "Box Plot"])

# Create a figure and axis object using Matplotlib
fig, ax = plt.subplots()

# Create the plot based on the selected plot type
if plot_type == "Bar Plot":
    x_axis = "state"
    y_axis = "modal_price"
    sns.barplot(data=filtered_data, x=x_axis, y=y_axis, ax=ax)
elif plot_type == "Line Plot":
    x_axis = "market"
    y_axis = "modal_price"
    sns.lineplot(data=filtered_data, x=x_axis, y=y_axis, ax=ax)
elif plot_type == "Box Plot":
    x_axis = "market"
    y_axis = "modal_price"
    sns.boxplot(data=filtered_data, x=x_axis, y=y_axis, ax=ax)

# Set the plot title and axis labels
ax.set_title(f"{plot_type} of {commodity} Prices")
ax.set_xlabel(x_axis.capitalize())
ax.set_ylabel("Modal Price")

# Display the plot using Streamlit
st.pyplot(fig)

# Load the CSV data
data = pd.read_csv("Kaggle.csv")

# Define the column names for the X and Y axis options
x_axis_options = ["state", "market", "commodity", "min_price", "max_price"]
y_axis_options = ["state", "market", "commodity", "min_price", "max_price"]

# Ask the user to select the X and Y axis coordinates
x_axis = st.selectbox("Select X-axis coordinate", x_axis_options)
y_axis = st.selectbox("Select Y-axis coordinate", y_axis_options)

# Generate a scatter plot
if st.button("Scatter plot"):
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

# Generate a line plot
if st.button("Line plot"):
    fig, ax = plt.subplots()
    sns.lineplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

# Generate a bar chart
if st.button("Bar chart"):
    fig, ax = plt.subplots()
    sns.barplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

# Generate a histogram
if st.button("Histogram"):
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

# Generate a box plot
if st.button("Box plot"):
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)

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
