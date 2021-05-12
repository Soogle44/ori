import streamlit as st


st.title("Oriental Lounge Tracker")
link = '[Oriental Lounge](https://oriental-lounge.com/)'
st.markdown(link, unsafe_allow_html=True)

show_date = st.date_input("input date")

st.write(type(show_date))
st.write(show_date.day)
st.write(type(show_date.day))
