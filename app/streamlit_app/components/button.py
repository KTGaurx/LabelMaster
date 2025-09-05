import streamlit as st


def create_project_button():
    if st.button("Create Project"):
        with st.form("create_project_form", clear_on_submit=True):
            name = st.text_input("Project Name")
            description = st.text_area("Description")
            submitted = st.form_submit_button("Create")
            if submitted:
                st.success(f"Project '{name}' created successfully!")
