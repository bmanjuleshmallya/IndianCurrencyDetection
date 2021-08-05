# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:05:19 2021

@author: DELL LAPTOP
"""

import streamlit as st
from PIL import Image
st.title("Indian Currency Classifier")
st.header("Classifies 7 types of Indian Currency 10,20,50,100,200,500,2000")
st.text("")
st.text("Upload image of Indian Currency note")

from img_classification import currency_classification

uploaded_file = st.file_uploader("upload here",type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Note', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    st.write("Just a minute")
    label = currency_classification(image, 'model_classifier.h5')
    switcher = {
             0 : "hundred", 
             1: "two hundred",
             2: "two thousand",
             3: "five hundred",
             4: "fifty",
             5: "ten",
             6: "twenty"
    }
    s=switcher.get(label, "Not Maching")
    st.write("Done..")
    if s=="Not Maching":
        st.write("Enter valid Image")
    else :
        st.write("This is ", s," rupees note")