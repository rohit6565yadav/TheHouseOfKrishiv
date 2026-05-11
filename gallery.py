from email.mime import image

import streamlit as st
import numpy as np
import base64 as b64
from pathlib import Path

product_id = st.query_params.get("id")
product_name = st.query_params.get("product")

# Helper function to convert local image to base64
def get_base64_image(image_path):
    img_bytes = Path(image_path).read_bytes()
    return b64.b64encode(img_bytes).decode()
# Sample images
if product_id == '1':
    images = np.array([
        "images/elegant_ethnic_wear_kurti.jpg",
        "images/elegant_ethnic_wear_kurti.jpg",
        "images/elegant_ethnic_wear_kurti.jpg",
        "images/elegant_ethnic_wear_kurti.jpg",
        "images/elegant_ethnic_wear_kurti.jpg",
    ])
elif product_id == '2':
    images = np.array([
        "images/blue_embrodered_connon_anarkali.jpg",
        "images/blue_embrodered_connon_anarkali.jpg",
        "images/blue_embrodered_connon_anarkali.jpg",
        "images/blue_embrodered_connon_anarkali.jpg",
        "images/blue_embrodered_connon_anarkali.jpg",
    ])
elif product_id == '3':
    images = np.array([
        "images/contton_suit_set_with_duppatta.jpg",
        "images/contton_suit_set_with_duppatta.jpg",
        "images/contton_suit_set_with_duppatta.jpg",
        "images/contton_suit_set_with_duppatta.jpg",
        "images/contton_suit_set_with_duppatta.jpg",
    ])
elif product_id == '4':
    images = np.array([
        "images/elegant_cotton_suit_with_duppata.jpg",
        "images/elegant_cotton_suit_with_duppata.jpg",
        "images/elegant_cotton_suit_with_duppata.jpg",
        "images/elegant_cotton_suit_with_duppata.jpg",
        "images/elegant_cotton_suit_with_duppata.jpg",
    ])
else :
    images = np.array([])

st.set_page_config(layout="wide")
st.title(product_name)

# Session state
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Current image
if len(images) == 0:
    st.warning("No images found.")
    st.stop()

# Initialize index
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Keep index within bounds
st.session_state.current_index = max(
    0,
    min(st.session_state.current_index, len(images) - 1)
)

# Safe access
current_img = images[st.session_state.current_index]

# ---------- Main Image ----------
st.image(current_img, use_container_width=True)

# ---------- Navigation Buttons ----------
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Previous"):
        st.session_state.current_index = (
            st.session_state.current_index - 1
        ) % len(images)
        st.rerun()

with col3:
    if st.button("Next ➡"):
        st.session_state.current_index = (
            st.session_state.current_index + 1
        ) % len(images)
        st.rerun()

# ---------- Thumbnail Strip ----------
st.markdown("### Thumbnails")

thumb_cols = st.columns(len(images))

for i, img in enumerate(images):

    with thumb_cols[i]:

        # Highlight active thumbnail
        border = "5px solid red" if i == st.session_state.current_index else "1px solid gray"
        img_base64 = get_base64_image(img)
        st.markdown(
            f"""
            <div style="
                border:{border};
                border-radius:10px;
                padding:3px;
            ">
                <img src="data:image/png;base64,{img_base64}" width="100%">
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(f"Select", key=f"thumb_{i}"):
            st.session_state.current_index = i
            st.rerun()