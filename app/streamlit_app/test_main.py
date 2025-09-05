import streamlit as st

# Page configuration
st.set_page_config(page_title="LabelMaster", page_icon="🏷️", layout="wide")

# Sidebar
st.sidebar.title("📌 Navigation")
choice = st.sidebar.selectbox("Go to", ["Home", "Upload", "Settings"])

st.sidebar.markdown("---")
st.sidebar.info("LabelMaster v1.0")

# Main content
if choice == "Home":
    st.title("🏷️ LabelMaster")
    st.write("Welcome to the LabelMaster dashboard.")
    st.write("Use the sidebar to switch between pages.")

elif choice == "Upload":
    st.title("📂 Upload Files")
    uploaded_file = st.file_uploader(
        "Choose a file", type=["png", "jpg", "jpeg", "pdf"]
    )
    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")

elif choice == "Settings":
    st.title("⚙️ Settings")
    theme = st.selectbox("Choose theme:", ["Light", "Dark", "Auto"])
    st.write(f"Selected theme: {theme}")
######################
import os

import streamlit as st
from pages import mainpage, page_1, page_2

# Page config
st.set_page_config(page_title="LabelMaster", page_icon="🏷️", layout="wide")

# Get list of projects
project_list = os.listdir("./app/database")

# Sidebar: Project selection first
st.sidebar.text("Project Selection")
selected_project = st.sidebar.selectbox("Select Project", project_list)

# Sidebar: Page navigation
st.sidebar.text("Navigation")
# Map pages
pages = {
    "Overview": [
        st.Page(mainpage.overview, title="Create your account"),
    ],
    "DataLabeling": [
        st.Page(page_1.DataOverview, title="Create your account"),
    ],
    "ModelTraining": [
        st.Page(page_2.ModelOverview, title="Learn about us"),
    ],
}

# Run the selected page
pg = st.navigation(pages)

if __name__ == "__main__":
    pg.run()
######################
