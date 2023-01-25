import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/portrait.png")

with col2:
    st.title("Chris Jamieson")
    content = """Hi, I'm Chris! I am a project manager exploring the critical role quality data plays in 
    manufacturing environments. I graduated in 2010 with a Bachelor of Science in Chemical Engineering from the 
    University of Washington. I have held roles at Janicki industries as the Director of Metrology and at Fluke 
    Corporation as an Operations Compliance Project Manager. """
    st.info(content)

blurb = """Below you can find some of the apps I have built in Python, Feel free to contact me!"""
st.write(blurb)
