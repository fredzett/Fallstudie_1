import pandas as pd 
import altair as alt
import streamlit as st
xrange = (0,100)



def make_chart(df):
    scatter = alt.Chart(df).mark_point(color="blue", size=100, opacity=.5).encode(
        alt.X("x",scale=alt.Scale(domain=(0,22))),
        alt.Y("y", scale=alt.Scale(domain=(0,300))),
        tooltip=["yhat", "y"],
    )
    line = alt.Chart(df).mark_line(color="green").encode(
        alt.X("x"),
        alt.Y("yhat"),
    
        
    )
    point = alt.Chart(df).mark_circle(color="black").encode(
            alt.X("x"),
            alt.Y("yhat"),   
            tooltip=["x"]
    )


    line2 = alt.Chart(df).mark_rule(color="black", ).encode(
            alt.X("x"),
            alt.Y("y"),
            alt.Y2("yhat"), 
    )

    return scatter, line, point, line2