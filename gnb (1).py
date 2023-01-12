#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
import numpy as np
from pickle import dump
from pickle import load


st.title( ':blue[Bankruptcy-Prevention]')

st.sidebar.header('User Input Parameters')
def user_input_features():
    industrial_risk= st.sidebar.selectbox('industrial_risk',('1.0','0.5','0.0'))
    management_risk = st.sidebar.selectbox('Managment_risk',('1.0','0.5','0.0'))
    financial_flexibility = st.sidebar.selectbox('financial_flexibility',('1.0','0.5','0.0'))
    credibility= st.sidebar.selectbox('credibility',('1.0','0.5','0.0'))
    competitiveness = st.sidebar.selectbox('competitiveness',('1.0','0.5','0.0'))
    operating_risk = st.sidebar.selectbox('operating_risk',('1.0','0.5','0.0'))
    data = {'Industrial_risk':industrial_risk,'Managment_risk':management_risk,'financial_flexibility': financial_flexibility,'credibility':credibility,'competitiveness':competitiveness,'operating_risk':operating_risk}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# load the model from disk
model = load(open("gnb.pkl",'rb'))
prediction = model.predict(df)
st.subheader('Predicted Result')
st.subheader('Detected As')

st.write('Yes' if prediction ==1.0 else 'No')
st.subheader('This Means')
st.write('Bankruptcy Detected' if prediction ==1.0 else 'Non-Bankruptcy Detected')


# In[ ]:




