import streamlit as st
from requests_html import HTMLSession
import pandas as pd

sess = HTMLSession()
API_URL = f"http://127.0.0.1:80/"


def get_data():
    fuel_prices_json = sess.get(API_URL).json()
    for records in fuel_prices_json:
        if records["brand"] is None or records["brand"] == "None":
            fuel_prices_json.remove(records)
    return pd.json_normalize(fuel_prices_json)

fuel_prices = get_data()

st.set_page_config(
    page_title="Fuel Prices Dashboard",
    page_icon="✅",
    layout="wide",
)

# dashboard title
st.title("Live Dashboard")
st.write(
    "You can see the data from the previous day (D-1) of gasoline in France on this dashboard"
)
# top-level filters
fuel_filter = st.selectbox("Select the type of fuel", ["E10", "SP98"])

if fuel_filter == "E10":
    e10_df = fuel_prices
    st.title("Average price per brand of E10 gasoline")
    e10_df = e10_df.dropna(subset=["price_e10", "brand"])
    e10_df = e10_df.groupby("brand", as_index=False)["price_e10"].mean()
    st.bar_chart(e10_df[["price_e10", "brand"]], y="price_e10", x="brand")
elif fuel_filter == "SP98":
    e10_df = fuel_prices
    st.title("Average price per brand of SP98 gasoline")
    e10_df = e10_df.dropna(subset=["price_sp98", "brand"])
    e10_df = e10_df.groupby("brand", as_index=False)["price_sp98"].mean()
    st.bar_chart(e10_df[["price_sp98", "brand"]], y="price_sp98", x="brand")
