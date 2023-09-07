# Simple Data Visualization App

This is a simple data visualization web application built using Streamlit in Python. The app allows users to upload CSV or Excel files, select columns for visualization, and generate various types of charts and plots based on the data.

## Features

- **Upload Data**: Users can upload CSV or Excel files containing their data.

- **Single-Variable Plots**:
  - Histogram: For numerical columns.
  - Countplot: For categorical columns.

- **Bivariate Plots**:
  - Scatter Plot: For two numerical columns.
  - Bar Plot: For two categorical columns.
  - Stacked Bar Plot: For two categorical columns.
  - Line Plot: For one numerical and one categorical column (X vs Y).

- **Title and Axes Labels**: All generated charts and plots include titles and axes labels for better understanding.

- **Bar Chart for Categorical vs. Numerical**: The app can generate bar charts when one of the selected columns is categorical and the other is numerical.

## Getting Started

1. Clone this repository to your local machine.

   ```shell
   git clone https://github.com/your-username/data-viz-app.git
   cd data-viz-app
