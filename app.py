import pandas as pd
import numpy as np
import streamlit as st
from confirm_button_hack import cache_on_button_press
import time


st.title('Test Confirm Button')
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
data = pd.read_csv(DATA_URL, nrows=50)

lon_slider = st.slider('long', 73.5, 74.0, step=0.1)
lat_slider = st.slider('lat', 40.0, 41.0, step=0.1)

data_f = data

@cache_on_button_press('Submit')
def filter_data_by_lon(df, lon_value):
     return df[df['Lon'] <= -lon_value]

data_f = filter_data_by_lon(data_f, lon_slider)
st.dataframe(data_f)



# @cache_on_button_press('Authenticate')
# def authenticate(username, password):
#     return username == "buddha" and password == "s4msara"
#
# username = st.text_input('username')
# password = st.text_input('password')
#
# if authenticate(username, password):
#     st.success('You are authenticated!')
#     st.write(st.slider('Test widget'))
# else:
#     st.error('The username or password you have entered is invalid.')


