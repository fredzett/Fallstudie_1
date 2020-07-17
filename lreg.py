import streamlit as st
import pandas as pd 
import numpy as np 
import altair as alt

from utils import make_chart

XMIN = 1
XMAX = 2

@st.cache
def make_data(X_sim,n=10):
    
    y = 100 + np.log2(X_sim)*20 + np.sin(5*X_sim) + np.random.random(n)*5*np.random.random()#*1000
    df = pd.DataFrame({"x":X_sim, "y":y})
    return df


st.markdown(f"""
### Problem 1:
### Problem 2: <a href='#Problem1'> [hier] </a>

""", unsafe_allow_html=True)



st.markdown("`Graph 1: Umsatz vs. Werbebudget`")
n = 10
X_sim = np.linspace(1,20,n)
b0 = st.sidebar.slider("b0",50,110,0)
b1 = st.sidebar.slider("w1",0,10,0)
show_deltas = st.sidebar.checkbox("Detlas?")

yhat = b0 + b1*X_sim
print(yhat)

df = (make_data(X_sim,int(n))
      .assign(yhat=yhat)
    )


a,b,c,d = make_chart(df)
if show_deltas:
    chart = a + b + c + d
else:
    chart = a + b 

chart = chart.properties(
                width=600
            ).configure_view(
                strokeOpacity=0
             ).configure_axis(
                 grid=False
             ).interactive()
st.altair_chart(chart)

st.latex(f"Gleichung lautet f(x) = {b0} + {b1} Werbung")

