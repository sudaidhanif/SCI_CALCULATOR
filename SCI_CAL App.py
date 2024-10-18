# Function to perform basic calculator operations
def basic_calculator():
    st.title("Basic Calculator")  # Title for calculator
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)  # First number input
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)  # Second number input
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])  # Dropdown to select operation

    # Perform the operation based on user input
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"  # Handle division by zero
    st.write(f"The result is: {result}")  # Output the result


# Streamlit App Logic
st.title("Scientific Graphical Calculator")  # Title for the whole app

# Select between basic calculator or graph plot
app_mode = st.selectbox("Choose mode", ["Basic Calculator", "Graph Plotter"])  # Dropdown to choose mode

# If the user selects "Basic Calculator"
if app_mode == "Basic Calculator":
    basic_calculator()  # Call the basic calculator function
else:
    # Existing logic for the graph plotter
    function_input = st.text_input("Enter a mathematical function (e.g., 'np.sin(x)')", value="np.sin(x)")
    x_min = st.number_input("Enter the minimum value of x", value=-10.0)
    x_max = st.number_input("Enter the maximum value of x", value=10.0)

    if st.button("Calculate and Plot"):
        plot_function(function_input, (x_min, x_max))  # Call the plot function
        st.write(f"Derivative: {calculate_derivative(function_input)}")  # Calculate and display the derivative


import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff

# Function to plot a mathematical function
def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(func)  # Evaluate the function
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'y = {func}', color='blue')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Graph of {func}")
    plt.legend()
    st.pyplot(plt)

# Function to calculate derivatives
def calculate_derivative(func):
    x = symbols('x')
    derivative = diff(func, x)
    return derivative
