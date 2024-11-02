import streamlit as st

# Title
st.title("First Streamlit App")  

from PIL import Image

st.subheader("Hey This is Sid")

image = Image.open("about_dp.png")
st.image(image, use_column_width=True) 

st.markdown("This is Markdown")

st.success("congrats !! run sucessful")

st.info("This is an info for you")

st.warning("This is warning")

st.error("Error: 404")

st.help(range)