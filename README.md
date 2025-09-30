# Simple Linear Regression with CRISP-DM

This project provides a simple yet illustrative example of linear regression, framed within the Cross-Industry Standard Process for Data Mining (CRISP-DM) methodology. The Python script `linear_regression_example.py` generates synthetic data, calculates regression coefficients, and visualizes the results, making it an excellent tool for understanding fundamental concepts of machine learning and data analysis.

## CRISP-DM Framework

The script's structure and comments are designed to mirror the six phases of the CRISP-DM model:

### 1. Business Understanding

- **Objective:** The primary goal is to model and understand the linear relationship between two variables, `X` and `Y`.
- **Application:** This script serves as an educational tool to demonstrate how linear regression can be used to predict a dependent variable (`Y`) based on an independent variable (`X`).

### 2. Data Understanding

- **Data Source:** The script generates its own synthetic data, so no external data sources are needed.
- **Data Generation:** The data is created using the linear equation `Y = a*X + b + noise`, where:
    - `a` is the slope.
    - `b` is the intercept.
    - `noise` is a random value from a normal distribution, simulating real-world data imperfections.

### 3. Data Preparation

- **Process:** The user is prompted to provide the parameters for data generation (`a`, `b`, `noise`, and the number of data points).
- **Output:** The script produces two NumPy arrays, `x` and `y`, which are ready for the modeling phase.

### 4. Modeling

- **Technique:** Simple linear regression is used to model the relationship between `X` and `Y`.
- **Implementation:** The script calculates the regression coefficients (intercept `b0` and slope `b1`) using the least-squares method. The resulting regression equation is `Y = b0 + b1 * X`.

### 5. Evaluation

- **Method:** The model is evaluated visually. The script generates a scatter plot of the original data points and overlays the calculated regression line.
- **Interpretation:** This visualization allows for a qualitative assessment of how well the model fits the data. A close fit between the regression line and the data points indicates a good model.

### 6. Deployment

- **Usage:** The script is self-contained and can be run from the command line.
- **Interaction:** Users can experiment by inputting different values for the slope, intercept, noise level, and number of data points to observe how these changes affect the regression model.

## How to Run the Script

1. **Prerequisites:** Ensure you have Python and the following libraries installed:
   - `numpy`
   - `matplotlib`

   You can install them using pip:
   ```bash
   pip install numpy matplotlib
   ```

2. **Execute the script:**
   ```bash
   python linear_regression_example.py
   ```

3. **Follow the prompts:** Enter the desired parameters for the data generation, or simply press Enter to use the default values.

## Example Output

When you run the script, it will print the CRISP-DM steps, the calculated regression coefficients, and then display a plot similar to this:

![Sample Regression Plot](https://i.imgur.com/8v3w3jG.png)
