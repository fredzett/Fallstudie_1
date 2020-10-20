import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=100, n_features=10)
old = range(11)
new = ["y"] +["w"+str(i) for i in range(11)]
data = np.concatenate((y.reshape(-1,1),X),axis=1)
df = (pd.DataFrame(data)
      .rename(columns=dict(zip(old,new)))
     )
df = df.reset_index()

chart1 = alt.Chart(df).mark_point(color="red").encode(
    alt.X('w1',title='Umsatz'),
    alt.Y("y"),
)
chart2 = alt.Chart(df).mark_line().encode(
    x = "w1",
    y = "y"
)

st.sidebar.title("Navigation")
st.title("Fallstudie - Regression")
st.markdown(r"""

### `A | Ausgangslage`

[hier](http://www.spiegel.de)  

[to come - Text über XY GmbH, die Umsatz steigern möchte. Wichtige Punkte:

- Umsatzsteigerung geht nur indirekt (Preis erhöhen, mehr verkaufen etc.)]


> Dies ist ein Blockquote


$f(\text{Werbung}) = b_0 + w_1\text{Werbung}$
""")

st.altair_chart((chart1 + chart2).properties(
    width=600,
    height=400).interactive())