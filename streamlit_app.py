# import libraries
import streamlit as st
import pandas as pd
import json
import numpy as np
import os
import random
import PIL
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")
# set page configuration
st.set_page_config(
page_title= "Tarot Reading",
layout="wide",
)
# front end elements of the web page
html_temp = """
<div style ="background-color:white;padding:13px">
<h1 style ="color:black;text-align:center;">Tarot Reading App</h1></div>
"""
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)
st.caption('by Valeria Filippou ')



from pyngrok import ngrok 
!ngrok authtoken [Enter your authtoken here]
!nohup streamlit run app.py & 

url = ngrok.connect(port = 8501)
url #generates our URL

!streamlit run --server.port 80 app.py >/dev/null #used for starting our server
