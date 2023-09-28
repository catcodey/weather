import streamlit as st
import subprocess

# List of required libraries
required_libraries = ["numpy", "pandas", "matplotlib","seaborn"]

# Check if the required libraries are installed
missing_libraries = [lib for lib in required_libraries if subprocess.call(['pip', 'show', lib]) != 0]

# Install missing libraries if any
if missing_libraries:
    st.write("Installing missing libraries...")
    for lib in missing_libraries:
        subprocess.call(['pip', 'install', lib])
    st.write("Libraries installed successfully!")

# Your Streamlit app code goes here
st.title("My Streamlit App")
import numpy as np
import pandas as pd
import seaborn as sns



# List of required libraries


