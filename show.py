import streamlit as st

st.title("Hello👋")
st.markdown(
    """ 
    点开的是超级无敌大傻蛋
    """
)

if st.button("Send balloons!"):
    st.balloons()
