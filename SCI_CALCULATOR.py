import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero!"

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return np.sqrt(x) if x >= 0 else "Error: Square root of negative number!"

def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))

def tan(x):
    return np.tan(np.radians(x))

def log(x):
    return np.log(x) if x > 0 else "Error: Logarithm of non-positive number!"

def plot_function(funcs, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    plt.figure(figsize=(10, 5))

    for func in funcs:
        if func == 'sin':
            y = sin(x)
            label = 'sin(x)'
        elif func == 'cos':
            y = cos(x)
            label = 'cos(x)'
        elif func == 'tan':
            y = tan(x)
            label = 'tan(x)'
        elif func == 'exp':
            y = np.exp(x)
            label = 'e^x'
        elif func == 'sqrt':
            y = square_root(x)
            label = 'sqrt(x)'
            plt.ylim(0, 10)  # Limit y-axis for sqrt plot

        plt.plot(x, y, label=label)

    plt.title('Graph of Functions')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    st.pyplot(plt)

# Streamlit app
st.title("Scientific Graphical Calculator")

st.sidebar.header("Select Operation")
choice = st.sidebar.selectbox("Choose an operation:", [
    "Addition", "Subtraction", "Multiplication", "Division", 
    "Exponentiation", "Square Root", "Sine", "Cosine", 
    "Tangent", "Logarithm", "Plot Functions"
])

if choice in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]:
    x = st.number_input("Enter first number:", value=0.0)
    y = st.number_input("Enter second number:", value=0.0)

    if choice == "Addition":
        st.write(f"Result: {add(x, y)}")
    elif choice == "Subtraction":
        st.write(f"Result: {subtract(x, y)}")
    elif choice == "Multiplication":
        st.write(f"Result: {multiply(x, y)}")
    elif choice == "Division":
        st.write(f"Result: {divide(x, y)}")
    elif choice == "Exponentiation":
        st.write(f"Result: {exponentiate(x, y)}")

elif choice == "Square Root":
    x = st.number_input("Enter number:", value=0.0)
    st.write(f"Square root of {x} = {square_root(x)}")

elif choice in ["Sine", "Cosine", "Tangent", "Logarithm"]:
    x = st.number_input("Enter angle or number:", value=0.0)
    if choice == "Sine":
        st.write(f"sin({x}) = {sin(x)}")
    elif choice == "Cosine":
        st.write(f"cos({x}) = {cos(x)}")
    elif choice == "Tangent":
        st.write(f"tan({x}) = {tan(x)}")
    elif choice == "Logarithm":
        st.write(f"log({x}) = {log(x)}")

elif choice == "Plot Functions":
    funcs = st.text_input("Enter functions to plot (separated by commas, e.g., sin, cos, tan, exp, sqrt):")
    if funcs:
        funcs_list = [f.strip() for f in funcs.split(',')]
        x_range = (-10, 10)  # Example range for plotting
        plot_function(funcs_list, x_range)
