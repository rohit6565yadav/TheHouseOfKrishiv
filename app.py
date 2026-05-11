import streamlit as st

# Define individual page objects
page_1 = st.Page("main.py", title="Home", icon=":material/home:")
page_2 = st.Page("gallery.py", title="gallery", icon=":material/add_circle:")

# Initialize navigation
pg = st.navigation([page_1, page_2])

# Set global configuration and run
st.set_page_config(page_title="My App", page_icon="🚀")
pg.run()