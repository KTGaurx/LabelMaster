# app/streamlit_app/pages/dashboard.py
from datetime import datetime

import pandas as pd
import streamlit as st
from components import button


# --- Sample Data ---
def overview(selected_project):
    projects = [
        {
            "name": "Project A",
            "description": "Detect objects in images",
            "date_created": "2025-08-01",
            "progress": 0.7,
        },
        {
            "name": "Project B",
            "description": "Classify documents",
            "date_created": "2025-08-15",
            "progress": 0.4,
        },
        {
            "name": "Project C",
            "description": "Segment medical images",
            "date_created": "2025-08-20",
            "progress": 0.9,
        },
    ]

    total_labeled_samples = 12345
    dataset_size = 25000
    trained_models = 3

    # --- Page Layout ---
    st.title("Overview / Dashboard")

    # Quick stats
    st.subheader("Quick Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Labeled Samples", total_labeled_samples)
    col2.metric("Dataset Size", dataset_size)
    col3.metric("Trained Models", trained_models)

    st.markdown("---")

    # Project list
    st.subheader("Project List")
    for project in projects:
        st.markdown(f"**{project['name']}**")
        st.write(project["description"])
        st.write(f"Created: {project['date_created']}")
        st.progress(project["progress"])
        st.markdown("---")

    # Navigation
    st.subheader("Navigation")
    nav_options = ["Dataset", "Labeling", "Training", "Export", "Analytics"]
    selected_nav = st.radio("Go to:", nav_options)

    st.markdown("---")

    # Create Project
    button.create_project_button()
