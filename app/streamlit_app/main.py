import os

import streamlit as st
from pages import mainpage, page_1, page_2

project_list = os.listdir("./app/database")
st.set_page_config(page_title="LabelMaster", page_icon="🏷️", layout="wide")

st.sidebar.text("Project Selection")
project = st.sidebar.selectbox("project", project_list)
pages = {
    "Overview": [
        st.Page(mainpage.overview(selected_project=project), title="Dashboard"),
    ],
    "DataLabeling": [
        st.Page(
            page_1.DataOverview(selected_project=project), title="Create your account"
        ),
    ],
    "ModelTraining": [
        st.Page(page_2.ModelOverview(selected_project=project), title="Learn about us"),
    ],
}
pg = st.navigation(pages)
if __name__ == "__main__":
    pg.run()
