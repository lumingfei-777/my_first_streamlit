import streamlit as st

st.title("Hello👋")
st.markdown(
    """ 
    wyx是傻蛋
    """
)

if st.button("Send balloons!"):
    st.balloons()
