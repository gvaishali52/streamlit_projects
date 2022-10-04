import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title (" this is my first project in data science, hope you will like..")
st.header("The Iris flower data set or Fisher's Iris data set is a multivariate data set ")
st.subheader("quantify the morphologic variation of Iris flowers of three related species.")
st.markdown("The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.")

st.caption("this is the caption")

st.subheader("Reading dataset")
data = pd.read_csv("IRIS.csv")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader("Sepal_length")
bins =  st.slider('bin', 1, 30, 17)
hist_values = np.histogram(data['sepal_length'])[0]
st.bar_chart(hist_values)

st.subheader("Sepal_width")
bins =  st.slider('bin', 2, 30, 17)
hist_values = np.histogram(data['sepal_width'],bins=bins)[0]
st.bar_chart(hist_values)


st.subheader("Petal_length")
bins =  st.slider('bin', 3, 30, 17)
hist_values = np.histogram(data['petal_length'])[0]
st.bar_chart(hist_values)


st.subheader("Petal_width")
bins =  st.slider('bin', 4, 30, 17)
hist_values = np.histogram(data['petal_width'])[0]
st.bar_chart(hist_values)

