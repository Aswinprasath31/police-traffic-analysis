import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# --- Database Connection ---
# Use st.cache_resource to cache the database connection
@st.cache_resource
def get_connection():
    host = 'localhost'
    port = '3306'
    database = 'securecheck'
    username = 'root'
    password = 'Rose@143' # <-- IMPORTANT: Replace with your database password
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine

engine = get_connection()

# --- Load Data ---
# Use st.cache_data to cache the data loading
@st.cache_data
def load_data():
    query = "SELECT * FROM traffic_stops"
    df = pd.read_sql(query, engine)
    # Convert time column to datetime objects
    df['stop_time'] = pd.to_datetime(df['stop_time'], format='%H:%M').dt.time
    return df

df = load_data()

# --- Page Configuration ---
st.set_page_config(
    page_title="SecureCheck Dashboard",
    page_icon="👮",
    layout="wide"
)

st.title("👮 SecureCheck: Police Check Post Digital Ledger")
st.markdown("An interactive dashboard for analyzing traffic stop data.")

# --- Sidebar Filters ---
st.sidebar.header("Filter Data Here:")
gender = st.sidebar.multiselect(
    "Select Driver Gender:",
    options=df["driver_gender"].unique(),
    default=df["driver_gender"].unique()
)

race = st.sidebar.multiselect(
    "Select Driver Race:",
    options=df["driver_race"].unique(),
    default=df["driver_race"].unique()
)

violation = st.sidebar.multiselect(
    "Select Violation Type:",
    options=df["violation"].unique(),
    default=df["violation"].unique()
)

# --- Filtered DataFrame ---
df_selection = df.query(
    "driver_gender == @gender & driver_race == @race & violation == @violation"
)

# --- Main Page ---

# Top KPI's
total_stops = df_selection.shape[0]
total_arrests = int(df_selection["is_arrested"].sum())
arrest_rate = f"{total_arrests / total_stops * 100:.2f}%" if total_stops > 0 else "0.00%"

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Stops", f"{total_stops:,}")
with col2:
    st.metric("Total Arrests", f"{total_arrests:,}")
with col3:
    st.metric("Arrest Rate", arrest_rate)

st.markdown("---")

# --- Charts ---
col1, col2 = st.columns(2)

with col1:
    # Gender Distribution
    gender_dist = df_selection['driver_gender'].value_counts()
    fig_gender = px.pie(
        gender_dist, 
        values=gender_dist.values, 
        names=gender_dist.index,
        title="<b>Gender Distribution of Drivers</b>",
        hole=.3, 
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    # Violation Types by Gender
    violation_by_gender = df_selection.groupby('violation')['driver_gender'].value_counts().unstack().fillna(0)
    fig_violation_gender = px.bar(
        violation_by_gender,
        barmode='stack',
        title="<b>Violations by Gender</b>",
        labels={'value': 'Count of Stops', 'violation': 'Violation Type'},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_violation_gender, use_container_width=True)

# --- Data Table ---
st.subheader("Raw Data View")
st.dataframe(df_selection.head(20))
