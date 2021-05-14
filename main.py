from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.title("Oriental Lounge Tracker")
link = '[Oriental Lounge](https://oriental-lounge.com/)'
st.markdown(link, unsafe_allow_html=True)

# try:
DATABASE_URL = 'postgresql://uobmebyzrrghgx:2f7245be13f63c9885c843551a27ea1d6ffa5dbb7b043df593ac0910d8455b61@ec2-18-233-83-165.compute-1.amazonaws.com:5432/davgkjq1u2a64q'
engine = create_engine(DATABASE_URL)

df = pd.read_sql(sql='SELECT * FROM data;', con=engine)

shops = []
for shop in df.columns[1::2]:
    shops.append(shop.replace("man_", ""))

show_shop_list = st.multiselect('select area(s)', shops)
show_date = st.date_input("select date")
# mode = st.radio("select mode", ("separate", "overlay"))

show_list = ["date"]
for shop in show_shop_list:
    show_list.append("man_" + shop)
    show_list.append("woman_" + shop)

for i, date in enumerate(df["date"]):
    if show_date.day == date.day and date.hour == 18:
        show_df = df.iloc[i:i + 66, :]
        show_df = show_df[show_list]
        break

# if mode == "separate":
#     figs = []
#     for i in (len(show_list) - 1) / 2:
#         fig = go.Figure()

# else:
fig = go.Figure()
for col in show_list:
    if col != "date":
        fig.add_trace(go.Scatter(
            x=show_df["date"], y=show_df[col], name=col))

fig.update_layout(legend={"x": 0, "y": -0.2, "yanchor": "top"})
fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})
st.plotly_chart(fig)

# except Exception as e:
#     st.info(e)
