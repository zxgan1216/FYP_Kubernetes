import streamlit as st
from frontend_node import app as node_app
from frontend_cpu import app as cpu_app
from frontend_memory import app as memory_app
from frontend_diskIO import app as diskio_app
from frontend_network import app as network_app

# Streamlit App Layout
st.set_page_config(page_title="Kubernetes Monitoring Dashboard", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    .header-container {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .sidebar-link {
        display: block;
        margin: 10px 0;
        padding: 10px;
        text-align: left;  
        font-size: 16px;
        font-weight: bold;
        border: 1px solid rgba(128, 128, 128, 0.5); /* Gray border with 50% opacity */
        border-radius: 5px;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .sidebar-link:hover {
        background-color: rgba(255, 128, 128); /* Slightly darker gray on hover */
        color: #ffffff; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "frontend_node"


# Sidebar for Navigation
with st.sidebar:
    st.markdown(
        """
        <div>
            <h2 style="color:#ffffff;">Navigation</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Node selection
    node = st.selectbox("Select Node", options=[f"Node {i}" for i in range(50)], index=0)

    # Graph Analysis Section
    st.markdown("### Introduction to this Page")
    if st.button("Introduction to the dataset"):
        st.session_state.page = "intro_dataset"
    if st.button("Introduction to Graph Analysis"):
        st.session_state.page = "intro_graph"
    if st.button("Introduction to the ML model"):
        st.session_state.page = "intro_ML"
    if st.button("Add data"):
        st.session_state.page = "add_data"

    # Graph Analysis Section
    st.markdown("### Graph Analysis")
    if st.button("Node"):
        st.session_state.page = "frontend_node"
    if st.button("CPU"):
        st.session_state.page = "frontend_cpu"
    if st.button("Memory"):
        st.session_state.page = "frontend_memory"
    if st.button("Disk IO"):
        st.session_state.page = "frontend_diskio"
    if st.button("Network"):
        st.session_state.page = "frontend_network"

    # Prediction Section
    st.markdown("### Prediction")
    if st.button("Anomaly Detection"):
        st.session_state.page = "frontend_anomaly_detection"
    if st.button("Predictive Maintenance"):
        st.session_state.page = "frontend_predictive_maintenance"
    
    st.markdown(
        """
        <div>
            <br/>
            <h5 style="color:#ffffff;">by Prof Teh & Gan</h5>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Handle Page Navigation Logic
if st.session_state.page == "frontend_node":
    node_app(node)
elif st.session_state.page == "frontend_cpu":
    cpu_app(node)
elif st.session_state.page == "frontend_memory":
    memory_app(node)
elif st.session_state.page == "frontend_diskio":
    diskio_app(node)
elif st.session_state.page == "frontend_network":
    network_app(node)
elif st.session_state.page == "frontend_anomaly_detection":
    st.write("Anomaly Detection Page")
elif st.session_state.page == "frontend_predictive_maintenance":
    st.write("Predictive Maintenance Page")