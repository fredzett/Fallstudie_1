import pandas as pd 
import numpy as np 
from datetime import datetime
import streamlit as st
import altair as alt

colors ={"lightgrey":"#FFFFFF",
        "darkgrey": "#9b9999",
         "pink":"#f63366"
         } 

def _calc_loss(w0,w1,X,y):
    return (1/2*len(X)) * sum((y - (w0 + w1 * X))**2)

def calc_loss_partial(df,w0=None,w1=None):
    'Calculates Loss based on n different w1'
    if (w0 is None) & (w1 is None): raise AttributeError("One parameter must be fixed")
    
    X = df["Werbung"].values
    y = df["Absatz"].values

    if w0 is None: #w1 has value meaning w0 is varied
        label = "w0"
        ws = np.arange(-60,70,0.10)
        losses = [_calc_loss(w,w1,X,y) for w in ws]
    else: # w0 has value meaning w1 is varied
        label = "w1"
        ws = np.arange(-5,20,0.10)
        losses = [_calc_loss(w0,w,X,y) for w in ws]

    df = pd.DataFrame({"Fehler": losses, label:ws}).round(3)
    return df


def load_regression_data(n,w0=5,w1=8):
    'Generates synthetic data for regression example'

    np.random.seed(12)
    X = np.linspace(1,10,num=n) + np.random.random()
    y = w0 + w1*X #+ np.random.random(n)*20
    df = pd.DataFrame({"Absatz":y, "Werbung":X}, index=range(1,n+1))
    return df


#@st.cache
def update_df(w0,w1,df, show_line):
    'Updates dataframe with yhat and (y-yhat) based on w0 and w1 input'
    if show_line: 
        df["Prognose"] = float(w0) + float(w1) *df["Werbung"]
        df["Schätzfehler"] = df["Absatz"]- df["Prognose"]
        df["Schätzfehler2"] = df["Schätzfehler"]**2 
    else:
        df["Prognose"] = 0
        df["Schätzfehler"] = 0
        df["Schätzfehler2"] = 0
    return df

def df_to_table(df):
    'Returns reduced and formated df for table printing'
    if df["Prognose"].sum() == 0:
        df = (df.iloc[:,[0,1]]
                    .applymap("{0:.2f}".format)
                #.set_index(df["Monat_str"])
            )
    else:
        df = (df.iloc[:,[0,1,2,3]] # explicit in case other columns are created
                    .applymap("{0:.2f}".format)
                #.set_index(df["Monat_str"])
            )
    return df




###### CHART 1
def plot_regression(df):
    'Returns components to plot regression based on updated dataframe'
    
    min_x, max_x = df["Werbung"].min(), df["Werbung"].max()
    min_y, max_y = df[["Absatz","Prognose"]].min().min(), df[["Absatz","Prognose"]].max().max(),
    
    
    scatter = alt.Chart(df.reset_index()).mark_circle(size=100,color=colors["darkgrey"]).encode(
        alt.X("Werbung", scale=alt.Scale(domain=(0.8*min_x, 1.1*max_x))),
        alt.Y("Absatz", scale=alt.Scale(domain=(-20,120))),#(0.9*min_y,1.1*max_y))),
        tooltip=[alt.Tooltip("index:Q", title="Datenpunkt"),
                alt.Tooltip("Absatz",format=".2f"),
                alt.Tooltip("Werbung",format=".2f")
                ]
    )
    line = alt.Chart(df).mark_line(color=colors["pink"],clip=True).encode(
        alt.X("Werbung"),
        alt.Y("Prognose", title="Absatz")
    )

    error = alt.Chart(df).mark_rule(color=colors["darkgrey"], clip=True).encode(
            alt.X("Werbung"),
           alt.Y("Prognose", title="Absatz"),#alt.Y2("Absatz_Prognose")
            alt.Y2("Absatz"),
    )
    return scatter, line, error

def show_regression(df, show_line, show_error, ph_chart, ph_msg):
    scatter, line, error = plot_regression(df)
    if show_line & show_error:
        chart = (scatter + line + error)
    if show_line & (not show_error):
        chart = (scatter + line)
    if show_error & (not show_line):
        chart = scatter
        ph_msg.info(":heavy_exclamation_mark: Bitte auch 'Gerade anzeigen' aktivieren :heavy_exclamation_mark:")
    if (not show_line) & (not show_error):
        chart = scatter
    chart = chart.properties(width=700, height=300, title="Absatz vs. Werbung")
    ph_chart.altair_chart(chart)


###### Chart 2
def plot_y_yhat(df):
    min_x, max_x = df["Absatz"].min(), df["Absatz"].max()
    scatter = alt.Chart(df).mark_circle(clip=True, color=colors["pink"]).encode(
        alt.X("Prognose",scale=alt.Scale(domain=(min_x,max_x))),
        alt.Y("Absatz",scale=alt.Scale(domain=(min_x,max_x)))
    )
    line = alt.Chart(df).mark_line(clip=True, color=colors["darkgrey"]).encode(
        alt.X("Absatz", scale=alt.Scale(domain=(min_x,max_x))),
        alt.Y("Absatz",scale=alt.Scale(domain=(min_x,max_x)))
    )
    return scatter, line

def show_y_yhat(df, show_line, show_error, ph_chart2):
    if show_line & show_error:
        scatter, line = plot_y_yhat(df)
        chart = (scatter + line)
        chart = chart.properties(width=700, height=300, title="Absatz vs. Prognose (Absatz)")
        ph_chart2.altair_chart(chart)
    else:
        pass
    

def plot_loss_w1(df,w0, w1):
    'Plots error for varied w1s'
    losses = calc_loss_partial(df, w0=w0,w1=None) 
    line = alt.Chart(losses).mark_line().encode(
        alt.X("w1"),
        alt.Y("Fehler")
    )
    loss = losses[losses["w1"]==w1]
    point = alt.Chart(loss).mark_circle(size=200,color=colors["pink"]).encode(
        alt.X("w1"),
        alt.Y("Fehler")
    )
    return (line + point)

def plot_loss_w0(df,w0, w1):
    'Plots error for varied w0s'
    losses = calc_loss_partial(df, w0=None,w1=w1) 
    line = alt.Chart(losses).mark_line().encode(
        alt.X("w0"),
        alt.Y("Fehler")
    )
    loss = losses[losses["w0"]==w0]
    point = alt.Chart(loss).mark_circle(size=200,color=colors["pink"]).encode(
        alt.X("w0"),
        alt.Y("Fehler")
    )
    return (line + point)

def plot_error_bars(df):
    summe = df["Schätzfehler2"].sum() / len(df["Schätzfehler2"])
    errors = df["Schätzfehler2"].values
    new = pd.DataFrame(np.hstack((errors,summe)),columns=["Schätzfehler2"])
    new["Label"] = [f'{i:02d}' for i in list(range(1,len(new)))] + ["MSE"] # Hack to sort labels correctly?!?!?!

    bar = alt.Chart(new).mark_bar(size=40,color=colors["pink"], clip=True).encode(
         alt.X("Label", title="Datenpunkt"),
         alt.Y("Schätzfehler2", title="(Absatz - Prognose)^2", scale=alt.Scale(domain=(0,20_000))),
         color=alt.condition(
             alt.datum["Label"] == "MSE",
             alt.value(colors["pink"]),
             alt.value(colors["darkgrey"]),
         )
    )

    return bar




################ CONTOUR PLOT

#@st.cache
def calc_losses(b0,w1, X,y):
    losses = np.zeros((len(b0),(len(w1))))
    row = 0
    for b in b0:
        col = 0
        for w in w1:
            losses[row,col] = (1/(2*len(X)))*np.sum((y - (b+w*X))**2) #TODO: use own function
            col +=1
        row+=1
    return losses

@st.cache
def make_meshgrid(df):
    X = df["Werbung"].values
    y = df["Absatz"].values
    b0 = np.arange(0.0,10.3,0.3)
    w1 = np.arange(0.0,10.3,0.3)
    losses = calc_losses(b0,w1,X,y)
    b0,w1 = np.meshgrid(b0,w1)
    return b0,w1,losses


#@st.cache
def make_df(b0,w1,losses):
    b, w,l  = b0.ravel(order='F'),w1.ravel(order="F"), losses.ravel(order="C")
    df = pd.DataFrame({"w0":b,"w1":w,"Fehler":l})
    df = df.sort_values(by="Fehler", ascending= False).round(2)
    return df
#@st.cache
def plot_heatmap(df, w0,w1):
    #df = df[(df["w0"]>3) & (df["w0"]<6)]
    #df = df[(df["w1"]>6) & (df["w1"]<9)]
    contour = alt.Chart(df).mark_square(size=400, opacity=0.6, clip=True).encode(
                alt.X("w1"),#,scale=alt.Scale(domain=(-2,2))),
                alt.Y("w0"),#,scale=alt.Scale(domain=(-2,2))),
                tooltip=[alt.Tooltip("Fehler", title="Fehler", format=".2f"),
                        alt.Tooltip("w0",format=".2f"),
                        alt.Tooltip("w1",format=".2f")
                        ],
                color=alt.Color('Fehler',
                            scale=alt.Scale(range=["#14b1ab","#f3ecc2","#f9d56e","#e8505b"]))
                )                       #
                                        #["lightgreen","green","orange","red","lightblue","blue" ]

    df_show = df[(df["w0"]==float(w0)) & (df["w1"]==float(w1))]
    point = alt.Chart(df_show).mark_square(size=300,color="black", opacity=1).encode(
                alt.X("w1", axis=alt.Axis(grid=False), scale=alt.Scale(domain=(0,10))), 
                alt.Y("w0",axis=alt.Axis(grid=False), scale=alt.Scale(domain=(0,10))),
                tooltip="Fehler"
            ) 
    return (contour+point).properties(width=800, height=500).configure_view(strokeWidth=0)