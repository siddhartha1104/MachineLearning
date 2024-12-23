import matplotlib
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import model_selection

matplotlib.use('Agg')

from PIL import Image



st.title('My First ML App')
image = Image.open('bg.png')
st.image(image, use_column_width=True)

def main():
    activities = ['EDA', 'Visualisation', 'model', 'About us']
    option = st.sidebar.selectbox('Select Option:',activities)

    if option == 'EDA':
        st.subheader("Exploratory Data Analysis (EDA)")

        data = st.file_uploader('Upload dataset: ', type=['csv','xlsx','txt','json'])
        st.success("Data successfullu loaded")

        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head(50))

            if st.checkbox("Display shape"):
                st.write(df.shape)
            
            if st.checkbox('Display Null Values'):
                st.write(df.isna().sum())
            
            if st.checkbox("display the data types: "):
                st.write(df.dtypes)
            
            if st.checkbox("Display columns"):
                st.write(df.columns)
            
            if st.checkbox("Select multiple columns"):
                selected_columns = st.multiselect('select preferred columns:', df.columns)
                df1 = df[selected_columns]
                st.dataframe(df1)
            
            if st.checkbox("Display summary of original dataset"):
                st.write(df.describe().T)
            
            if st.checkbox("Display summary of selected dataset"):
                st.write(df1.describe().T)
            
            if st.checkbox("Display Correlation of data various columns: "):
                st.write(df.corr())
            
            
            

    elif option == 'Visualisation':
        st.subheader("Data Visualisation")

        data = st.file_uploader("upload dataset: ", type=['csv','xmls'])

        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("See all data"):
                st.dataframe(df)
            
            # if st.checkbox("see null values"):
            #     st.write(df.isna().sum())
            
            # if st.checkbox("check dtype"):
            #     st.write(df.dtypes)


            if st.checkbox("select multiple columns to plot"):
                selected_columns = st.multiselect('Select your preferred columns', df.columns)
                df1 = df[selected_columns]
                st.dataframe(df1)

            if st.checkbox("Display Heatmap"):
                st.write(sns.heatmap(df1.corr(), vmax=1, square=True, annot=True, cmap='viridis'))
                st.pyplot()


            

    
    # if option == 'model':


    # if option == 'About us':
if __name__ == '__main__':
    main()
     