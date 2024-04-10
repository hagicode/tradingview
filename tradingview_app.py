import streamlit as st
import requests

# ウェブサイトのURL
url = "https://sekai-kabuka.com/shikyou.html"

# ウェブサイトの内容を取得
response = requests.get(url)

# Streamlitで表示
st.write(response.text)
