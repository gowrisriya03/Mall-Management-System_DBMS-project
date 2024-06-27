import streamlit as st
import pandas as pd

from database1 import totalproduct

def total_product_frontend():
    st.empty()
    result = totalproduct()
    df = pd.DataFrame(result, columns=["Product ID", "Quantity", "Name","Type","Price","Total_Val"])
    st.dataframe(df)