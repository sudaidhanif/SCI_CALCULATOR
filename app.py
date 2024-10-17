import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Title of the app
st.title("Scientific Graphical Calculator")

# User input for function and range
function_input = st.text_input("Enter a function of x (e.g., 'x**2 + 3*x + 2'):")
x_min = st.number_input("Enter the minimum x value for plotting:", value=-10)
x_max = st.number_input("Enter the maximum x value for plotting:", value=10)

# Function to plot a mathematical function
def plot_function(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = eval(func)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=f'y = {func}', color='blue')
    plt.title('Function Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    st.pyplot(plt)

# Function to calculate the derivative of a given function
def calculate_derivative(func):
    x = sp.symbols('x')
    derivative = sp.diff(func, x)
    return derivative

if st.button("Calculate"):
    if function_input:
        # Plot the function
        plot_function(function_input, (x_min, x_max))

        # Calculate the derivative
        derivative_result = calculate_derivative(function_input)
        st.write(f"The derivative of {function_input} is: {derivative_result}")
    else:
        st.error("Please enter a valid function.")
