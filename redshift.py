import redshift_connector
import streamlit as st
import pandas as pd


class Redshift:
    def __init__(self, database: str):
        self.conn = redshift_connector.connect(
            host=st.secrets["redshift"]["host"],
            port=st.secrets["redshift"]["port"],
            user=st.secrets["redshift"]["user"],
            password=st.secrets["redshift"]["password"],
            database=database,
        )

    def query(self, query: str, ttl: int = 60, **kwargs) -> pd.DataFrame:
        @st.cache_data(
            show_spinner="Running `Redshift.query(...)`.",
            ttl=ttl,
        )
        def _query(query: str) -> pd.DataFrame:
            return pd.read_sql(query, con=self.conn, **kwargs)

        return _query(query)
