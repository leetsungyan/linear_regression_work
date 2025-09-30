# Interactive Linear Regression App

This is a Streamlit web application that demonstrates simple linear regression interactively. Users can adjust parameters to generate synthetic data, and the app will display the true regression line, the fitted regression line, and the calculated regression equation in real-time.

## Features

*   **Interactive Data Generation:** Adjust the slope, intercept, noise level, and number of data points using sliders.
*   **Real-time Visualization:** See the scatter plot, true line, and fitted regression line update instantly.
*   **Regression Equation:** View the calculated intercept and slope of the fitted regression line.

## How to Run Locally

1.  **Ensure Python is installed:** This application requires Python 3.7 or higher.

2.  **Install dependencies:** Navigate to the project directory in your terminal and install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This command will open the application in your default web browser. If it doesn't open automatically, navigate to `http://localhost:8501`.

## Deployment

This application can be easily deployed to the [Streamlit Community Cloud](https://streamlit.io/cloud) or other cloud platforms.

### Steps for Streamlit Community Cloud:

1.  **Push to GitHub:** Ensure your project (at least `app.py` and `requirements.txt`) is pushed to a public GitHub repository.
2.  **Sign Up/Log In:** Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign up or log in.
3.  **Deploy an App:** Click on "New app" and connect your GitHub repository. Select the `app.py` file as your main application file.
4.  **Deploy!** Click the "Deploy!" button, and your app will be live.