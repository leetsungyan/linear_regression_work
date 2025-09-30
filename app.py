
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_data(a, b, noise, num_points):
    """
    Generate synthetic linear data: Y = a*X + b + noise
    """
    x = np.linspace(0, 10, num_points)
    y = a * x + b + np.random.normal(0, noise, num_points)
    return x, y

def calculate_regression_coefficients(x, y):
    """
    Calculate simple linear regression coefficients (intercept b0 and slope b1)
    """
    n = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    sum_xy = np.sum(y * x) - n * mean_y * mean_x
    sum_xx = np.sum(x * x) - n * mean_x * mean_x
    b1 = sum_xy / sum_xx
    b0 = mean_y - b1 * mean_x
    return b0, b1

def plot_regression(x, y, a_true, b_true, b0_fit, b1_fit):
    """
    Plot scatter data, true line, and regression line.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', marker='o', s=30, label='Data Points')
    
    # True line
    y_true = a_true * x + b_true
    ax.plot(x, y_true, color='green', linestyle='--', label='True Line')
    
    # Regression line
    y_pred = b0_fit + b1_fit * x
    ax.plot(x, y_pred, color='red', label='Regression Line')
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Simple Linear Regression')
    ax.legend()
    ax.grid(True)
    return fig

# --- Streamlit App ---

st.title("Interactive Linear Regression")

# --- Sidebar for User Inputs ---
st.sidebar.header("Data Generation Parameters")
num_points = st.sidebar.slider("Number of data points:", 5, 500, 50)
a_true = st.sidebar.slider("Slope (a):", -5.0, 5.0, 2.0)
b_true = st.sidebar.slider("Intercept (b):", -5.0, 5.0, 1.0)
noise = st.sidebar.slider("Noise Level:", 0.0, 10.0, 1.0)

# --- Main App Content ---

# 1. Generate Data
x, y = generate_data(a_true, b_true, noise, num_points)

# 2. Modeling
b0_fit, b1_fit = calculate_regression_coefficients(x, y)

st.write("### Calculated Regression Coefficients")
st.write(f"**Intercept (b0):** {b0_fit:.4f}")
st.write(f"**Slope (b1):** {b1_fit:.4f}")
st.write(f"**Regression Equation:** Y = {b0_fit:.4f} + {b1_fit:.4f} * X")

# 3. Evaluation
st.write("### Regression Plot")
fig = plot_regression(x, y, a_true, b_true, b0_fit, b1_fit)
st.pyplot(fig)
