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

def plot_regression_line(x, y, b0, b1):
    """
    Plot scatter data and regression line
    """
    plt.scatter(x, y, color='blue', marker='o', s=30, label='Data Points')
    y_pred = b0 + b1 * x
    plt.plot(x, y_pred, color='red', label='Regression Line')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("=== Simple Linear Regression with CRISP-DM Steps ===\n")

    # --- 1. Business Understanding ---
    print("Step 1: Business Understanding")
    print("We aim to model the relationship between X and Y using a linear function Y = a*X + b + noise.\n")

    # --- 2. Data Understanding & 3. Data Preparation ---
    print("Step 2 & 3: Data Understanding and Preparation")
    try:
        a = float(input("Enter the slope (a) for Y = a*X + b: "))
        b = float(input("Enter the intercept (b): "))
        noise = float(input("Enter the noise level (e.g., 1.0): "))
        num_points = int(input("Enter the number of data points: "))
    except ValueError:
        print("Invalid input. Using default values: a=2, b=1, noise=1.0, num_points=10")
        a, b, noise, num_points = 2, 1, 1.0, 10

    x, y = generate_data(a, b, noise, num_points)
    print(f"\nGenerated {num_points} data points with noise level {noise}.\n")

    # --- 4. Modeling ---
    print("Step 4: Modeling")
    b0, b1 = calculate_regression_coefficients(x, y)
    print(f"Calculated Regression Coefficients:")
    print(f"Intercept (b0): {b0:.4f}")
    print(f"Slope (b1): {b1:.4f}")
    print(f"Regression Equation: Y = {b0:.4f} + {b1:.4f} * X\n")

    # --- 5. Evaluation ---
    print("Step 5: Evaluation")
    print("Plotting the scatter data and regression line...")
    plot_regression_line(x, y, b0, b1)

    # --- 6. Deployment ---
    print("Step 6: Deployment / Usage")
    print("You can modify slope, intercept, noise, or number of points to generate new data and observe regression.\n")
    print("=== Program Finished ===")

if __name__ == "__main__":
    main()