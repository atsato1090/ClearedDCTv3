import streamlit as st
from streamlit_lottie import st_lottie
import requests
import webbrowser

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title="ClearedDCT",
    page_icon="✈️",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #e6f2ff;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    h1 {
        color: #003366;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

clouds_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_pprxh53t.json")
st_lottie(clouds_animation, speed=1, height=200)

st.image("logo.png", width=300)
st.title("Welcome to ClearedDCT")

if st.button("🚀 ENTER APP", use_container_width=True):
    webbrowser.open("http://localhost:8501/cleareddct_tabs")  # Local use
    st.success("Opening ClearedDCT...")

st.info("Prepare for takeoff with your advanced ATC training assistant.")
