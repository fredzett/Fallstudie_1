import streamlit as st
import pandas as pd 
import numpy as np 
import altair as alt

from utils import *
import SessionState

#session = SessionState.get(run_id=0)
###################################################################################
### LOAD & PREPARE DATA
###################################################################################
df = simulate_regression_data()

###################################################################################
### SIDEBAR VIEW
###################################################################################
st.sidebar.header("Lineare Regression")
b0 = st.sidebar.slider(f"Achsenabschnitt (b0)", -10.0,10.0,0.0,0.1)
w1 = st.sidebar.slider("Steigung (w1)", -10.0,10.0,0.0,0.1)
show_deltas = st.sidebar.checkbox("Detas anzeigen?", False)




###################################################################################
### PAGE VIEW
###################################################################################
st.markdown("""
# Fallstudie 1  
Ziel der Fallstudie ist anhand eines interaktiven und visualisierten Beispiels die Grundprinzipien
des Maschinellem Lernen zu erläutern und insbesondere folgende Frage zu beantworten:  
> **Frage:** Wie lernt eine Maschine bzw. ein Computer?  

---  
# Absatzprognose der Fashion GmbH

# Ausgangslage  
[Einfügen - Text zur Fallstudie]
""")
st.markdown("""#### Daten:""")
table = st.empty()
#st.table(df_to_table(df))


st.markdown("# Analyse")
st.markdown("""## Absatz vs. Werbeausgaben:""")
show_vlines = False
if show_deltas:
    show_vlines = True
else:
    show_vlines = False

df = update_df(b0,w1,df)
table.table(df_to_table(df)) # Input data into table "placeholder"

chart = chart_regression(b0,w1,df, show_vlines=show_vlines)
st.altair_chart(chart)
color = "green"
st.success(f'''
Schätzung = **{b0}** + **{w1}** x Werbeaufwand
''')#,unsafe_allow_html=True)


st.markdown("""## Analyse des Schätzfehlers""")
chart1 = chart_w1_loss(b0,w1,df)
chart2 = chart_b0_loss(b0,w1,df)
chart = alt.hconcat(chart1.properties(width=350), chart2.properties(width=350))
bar = chart_yminushat(df)
chart_total = alt.vconcat(chart, bar.properties(width=750))
st.altair_chart(chart_total)


st.markdown("""## Gradient descent""")
#calc_gradient = st.checkbox("Schätze Parameter via Gradient Descent")

#if calc_gradient:
epochs = st.number_input("Anzahl der Iterationen",min_value=1,max_value=1000, step=10)
solution, losses, wses = gradient_descent(0,0,df, lr=0.01, epochs=1001)
chart = chart_loss_by_epochs(losses[:epochs]) # Calcuation performed at "gradient_descent"; only number of epochs shown changed
st.altair_chart(chart)

chart = chart_regression_gd(df,wses[epochs])

st.altair_chart(chart)
st.success(f'''
    Schätzung = **{wses[epochs][0]}** + **{wses[epochs][1]}** x Werbeaufwand
''')#,unsafe_allow_html=True)

