import streamlit as st 

def print(text:str,align:str="justify",linebreak:bool=True):
    if linebreak:
        msg = f"<p></p><div style='text-align:{align}'>{text}</div>"
    else:
        msg = f"<div style='text-align:{align}'>{text}</div>"
    return st.markdown(msg, unsafe_allow_html=True)
