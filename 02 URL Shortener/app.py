# REQUIRED PACKAGES
# pip install pyshorteners streamlit pyperclip

import pyshorteners
import streamlit as st

st.title("🔗 Welcome to URL Shortener")

# Streamlit input box
url = st.text_input("Enter the URL")

def url_shortener(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# Button to trigger shortening
if st.button("Shorten URL"):
    if url:
        short_url = url_shortener(url)
        st.success(f"Short URL: {short_url}")
    else:
        st.warning("Please enter a URL")