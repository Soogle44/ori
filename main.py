from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import plotly.express as px


DATABASE_URL = 'postgresql://uobmebyzrrghgx:2f7245be13f63c9885c843551a27ea1d6ffa5dbb7b043df593ac0910d8455b61@ec2-18-233-83-165.compute-1.amazonaws.com:5432/davgkjq1u2a64q'
engine = create_engine(DATABASE_URL)

df = pd.read_sql(sql='SELECT * FROM data;', con=engine)

shops = []
for shop in df.columns[1::2]:
    shops.append(shop.replace("man_", ""))

st.title("Oriental Lounge Tracker")
link = '[Oriental Lounge](https://oriental-lounge.com/)'
st.markdown(link, unsafe_allow_html=True)

show_shop_list = st.multiselect('select area', shops)
# show_date_list = st.multiselect('select date')

show_list = []
for shop in show_shop_list:
    show_list.append("man_" + shop)
    show_list.append("woman_" + shop)

if show_list != []:
    st.write(px.line(df, x='date', y=show_list))

else:
    st.info("select area")
