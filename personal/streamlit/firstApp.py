import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets
from sklearn.decomposition import PCA

from PIL import Image


st.title("My First Streamlit App")
image = Image.open('about_dp.png')
image

st.write("""## A simple data App with streamlit""")

st.write("Lets Explore different classifiers and datasets")
