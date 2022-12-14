import requests
import streamlit as st
import pandas as pd
from urllib.request import Request,urlopen
from streamlit_lottie import st_lottie

st.set_page_config(page_title="ICC Cricket Ranking", page_icon=":cricket_bat_and_ball:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

Load Assets
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_1fXD2hXInk.json")

req = Request('https://sports.ndtv.com/cricket/icc-rankings',headers={'user-Agent':'Mozilla/5.0'})
webpage = urlopen(req)
data = pd.read_html(webpage,header=0)

image_url = "data:image/jpeg;base64,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"
st.slider.image:st.sidebar.image(image_url,use_column_width=True)
st.markdown("<h1 style='text-align: center; color: black;'>Cricket ICC Ranking</h1>", unsafe_allow_html=True)
# st.title('Cricket ICC Ranking')

col1,col2,col3 = st.columns([0.5,2,0.5])
with col1:
    st_lottie(lottie_coding, height=250,key='coding')

with col2:
    menu1 = ["Team","Player"]
    a = st.sidebar.selectbox('Select',menu1)
    if a=="Team":
        menu2 = ["Test","ODI","T20"]
        b = st.sidebar.selectbox("Formats",menu2)
        if b =="Test":
            df = data[0]
            st.dataframe(df)
        if b =="ODI":
            df = data[4]
            st.dataframe(df)
        if b =="T20":
            df = data[8]
            st.dataframe(df)
    if a=="Player":
        menu3=["Test","ODI","T20"]
        b = st.sidebar.selectbox("Format",menu3)
        if b=="Test":
            menu4=['Batting','Bowling','All Rounder']
            c = st.selectbox("Select",menu4)
            if c=="Batting":
                df=data[1]
                st.dataframe(df)
            if c=="Bowling":
                df=data[2]
                st.dataframe(df)
            if c=="All Rounder":
                df=data[3]
                st.dataframe(df)
        if b=="ODI":
            menu5=['Batting','Bowling','All Rounder']
            c = st.selectbox("Select",menu5)
            if c=="Batting":
                df=data[5]
                st.dataframe(df)
            if c=="Bowling":
                df=data[6]
                st.dataframe(df)
            if c=="All Rounder":
                df=data[7]
                st.dataframe(df)
        if b=="T20":
            menu6=['Batting','Bowling','All Rounder']
            c = st.selectbox("Select",menu6)
            if c=="Batting":
                df=data[9]
                st.dataframe(df)
            if c=="Bowling":
                df=data[10]
                st.dataframe(df)
            if c=="All Rounder":
                df=data[11]
                st.dataframe(df)
with col3:
    st_lottie(lottie_coding, height=250)

with st.expander("For More",expanded=False):
    st.write("[@cricbuzz](https://www.cricbuzz.com/)")
    st.info("Built with Streamlit")
    st.write("[@Kedar.B](https://www.linkedin.com/in/kedarbhingarde)")
    st.text("Kedar A. Bhingarde")

