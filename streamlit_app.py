import streamlit as st
import os

# Read the content of the HTML and CSS files
html_file_path = "index.html"
css_file_path = "styles.css"

# Read the HTML file and insert it into Streamlit
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

# Apply CSS file
with open(css_file_path, "r") as css_file:
    css_content = css_file.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Display the HTML content
st.markdown(html_content, unsafe_allow_html=True)
