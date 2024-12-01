import streamlit as st 
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import base64
import time

st.set_page_config(layout="wide") #landsacpe view

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)