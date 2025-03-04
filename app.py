import streamlit as st
import pandas as pd
from redshift import Redshift

conn = Redshift(database="analytics_storysolitaire")
ttl = 60

st.title("kayani")
st.write("Welcome to kayani!")

df = conn.query("SELECT * FROM data.payments LIMIT 10", ttl=ttl, index_col="event_time")
st.dataframe(df)
