import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
# Set the title of the app
st.title("Simple Data Visualization App")

# Allow users to upload CSV or Excel files
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    if uploaded_file.name.endswith('csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Display the uploaded data
    st.write("Uploaded Data:")
    st.write(df)

    # Select columns for chart
    selected_columns = st.multiselect("Select columns for chart", df.columns)

    if selected_columns:
        # Check if one or two columns are selected for plotting
        if len(selected_columns) == 1:
            col_name = selected_columns[0]

            st.write(f"### {col_name}")

            # Check data type of the selected column
            data_type = df[col_name].dtype

            if data_type == "object":
                # Countplot for categorical columns
                plt.figure(figsize=(10, 6))
                sns.countplot(data=df, x=col_name)
                plt.xlabel(col_name)
                plt.ylabel("Count")
                plt.title(f"Countplot of {col_name}")
                plt.xticks(rotation=45)
                st.pyplot()
            else:
                # Histogram for numerical columns
                plt.figure(figsize=(8, 6))
                plt.hist(df[col_name], bins=20)
                plt.xlabel(col_name)
                plt.ylabel("Frequency")
                plt.title(f"Histogram of {col_name}")
                st.pyplot()

        elif len(selected_columns) == 2:
            col1, col2 = selected_columns

            st.write(f"### Plot between {col1} and {col2}")

            # Check data types of selected columns
            col1_data_type = df[col1].dtype
            col2_data_type = df[col2].dtype

            if col1_data_type == "object" and col2_data_type == "object":
                # Countplot for two categorical columns
                plt.figure(figsize=(10, 6))
                sns.countplot(data=df, x=col1, hue=col2)
                plt.xlabel(col1)
                plt.ylabel("Count")
                plt.title(f"Countplot of {col1} by {col2}")
                plt.xticks(rotation=45)
                st.pyplot()

            elif col1_data_type != "object" and col2_data_type != "object":
                # Scatter plot for two numerical columns
                plt.figure(figsize=(8, 6))
                plt.scatter(df[col1], df[col2])
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.title(f"Scatter Plot between {col1} and {col2}")
                st.pyplot()

            elif col1_data_type == "object" and col2_data_type != "object":
                # Bar chart for a categorical column against a numerical column
                plt.figure(figsize=(10, 6))
                sns.barplot(data=df, x=col1, y=col2)
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.title(f"Bar Chart of {col1} vs {col2}")
                plt.xticks(rotation=45)
                st.pyplot()

            elif col1_data_type != "object" and col2_data_type == "object":
                # Bar chart for a categorical column against a numerical column
                plt.figure(figsize=(10, 6))
                sns.barplot(data=df, x=col2, y=col1)
                plt.xlabel(col2)
                plt.ylabel(col1)
                plt.title(f"Bar Chart of {col2} vs {col1}")
                plt.xticks(rotation=45)
                st.pyplot()

            else:
                st.write("Please select two numerical columns or two categorical columns for a bivariate plot.")

        else:
            st.write("Please select one or two columns for plotting.")
