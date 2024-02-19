# app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title='Predict',
    page_icon=':)',
    layout='wide'
)
st.title("Make a Prediction")