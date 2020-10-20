import streamlit as st
import pandas as pd 
import numpy as np

from sthelper import print
from chapters import show_ch1, show_ch2, show_ch3, show_not_implemented

##### Sidebar
chapter_choice = ["1. Einleitung", "2. Grundlagen Überwachtes Lernen", 
                  "3. Lineare Regression", "4. Maschinelles Lernen"]

st.sidebar.subheader("Kapitelauswahl")
chapter = st.sidebar.selectbox("", chapter_choice, index=0)
st.sidebar.markdown("---")

if chapter == chapter_choice[0]:
    show_ch1()
elif chapter == chapter_choice[1]:
    show_ch2()
elif chapter == chapter_choice[2]:
    show_ch3()
else:
    st.error("Uuups. Something went wrong!")