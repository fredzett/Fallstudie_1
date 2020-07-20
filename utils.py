import pandas as pd 
import numpy as np
import altair as alt
import streamlit as st 



### CHARTS
### all using altair package

config = {"width":700,"strokeopacity":0, "grid":False, "border":0}

def plot_line(x:str,y:str,df:pd.DataFrame, color="red"):
    'Generates simple altair line chart'
    return alt.Chart(df).mark_line(color=color).encode(
                alt.X(x),
                alt.Y(y),
            )
def plot_circle(x:str,y:str,df:pd.DataFrame, color="red"):
    'Generates simple altair circle chart'
    return alt.Chart(df).mark_circle(color=color).encode(
                alt.X(x),
                alt.Y(y),
            )
def plot_point(x:str,y:str,df:pd.DataFrame, color="red"):
    'Generates simple altair point chart'
    return alt.Chart(df).mark_point(color=color).encode(
                alt.X(x),
                alt.Y(y),
            )

def plot_vlines(x,y,y2,df,color="green"):
    'Generates simple altair rule chart'
    alt.Chart(df).mark_rule(color=color).encode(
            alt.X(x),
            alt.Y(y),
            alt.Y2(y2), 
    )


def chart_regression(b0,w1,df,show_vlines):
    'Produces chart showing Absatz vs. Werbeausgaben'
    #df["Absatz_Prognose"] = float(b0) + float(w1) *df["Werbeausgaben"] 
    df["Schätzfehler"] = df["Schätzfehler"]
    min_x, max_x = df["Werbeausgaben"].min(), df["Werbeausgaben"].max()
    min_y, max_y = -19,20#df.min().min(), df.max().max()
    points = alt.Chart(df).mark_circle(color="#434A56",size=100).encode(
            alt.X("Werbeausgaben",scale=alt.Scale(domain=(0.9*min_x,1.1*max_x))),
            alt.Y("Absatz",scale=alt.Scale(domain=(0.9*min_y,1.1*max_y))
                , title="Absatz"),
            tooltip= [alt.Tooltip(field="Schätzfehler",title="Schätzfehler",type="quantitative", format=".2f"),
                     alt.Tooltip(field="Absatz_Prognose", title="geschätzter Absatz", type="quantitative", format=".2f")
                    ]
    )
    line = alt.Chart(df).mark_line(color="#F63366", size=2).encode(
            alt.X("Werbeausgaben"),#,scale=alt.Scale(domain=(0.9*min_x,1.1*max_x))),
            alt.Y("Absatz_Prognose")#alt.Y("Absatz_Prognose")
    )
    vlines = alt.Chart(df).mark_rule(color="#434A56").encode(
            alt.X("Werbeausgaben"),
           alt.Y("Absatz_Prognose"),#alt.Y2("Absatz_Prognose")
            alt.Y2("Absatz"),
    )
    if (b0 == 0) & (w1 == 0):
        chart = points
    else:
        chart = points + line 
    if show_vlines: chart = chart + vlines
    return chart.properties(
                                width=780
                            ,   height=400
                            ).interactive()

def chart_w1_loss(b0,w1, df):
    df = _calc_loss_w1(b0,df)
    lines = alt.Chart(df).mark_line().encode(
        alt.X("w1"),
        alt.Y("Loss"),
    )
    df_w = df[df["w1"]==w1]
    point = alt.Chart(df_w).mark_circle(color="red",size=100).encode(
        alt.X("w1", title="w1"),
        alt.Y("Loss", title="Loss")
    )
    chart = lines + point
    return chart

def chart_b0_loss(b0,w1, df):
    df = _calc_loss_b0(w1,df)
    lines = alt.Chart(df).mark_line().encode(
        alt.X("b0"),
        alt.Y("Loss"),
    )
    df_w = df[df["b0"]==w1]
    point = alt.Chart(df_w).mark_circle(color="red",size=100).encode(
        alt.X("b0", title="b0"),
        alt.Y("Loss", title="Loss")
    )
    chart = lines + point
    return chart


def chart_yminushat(df):
    bar = alt.Chart(df).mark_bar(size=40, color="#F63366", opacity=1).encode(
        alt.X("Monat_num", title="Monate", ),
        alt.Y("Schätzfehler", title="y - yhat"), 
    )
    #text = bar.mark_text(
    #    align="center",
    #    baseline="middle",
    #    dx=50
    #).encode(text="Schätzfehler:Q"
    #Kdf["Schätzfehler2"] = df["Schätzfehler"]**2+0.01
    bar2 = alt.Chart(df).mark_bar(size=20, color="grey", opacity=0.1).encode(
        alt.X("Monat_num", title="Monate", ),
        alt.Y("Schätzfehler2", title="y - yhat"), 
    )
    return bar2 + bar

def chart_loss_by_epochs(losses):
    losses = (pd.DataFrame(losses, columns=["Schätzfehler"])
                .reset_index()
                .assign(index=lambda x: x.astype(int) + 1)
             )
    losses["Schätzfehler"] = losses["Schätzfehler"] / 1000
    min_y, max_y = losses["Schätzfehler"].min(), losses["Schätzfehler"].max()
    chart = alt.Chart(losses).mark_circle().encode(
        alt.X("index", title="Anzahl Iterationen",),
        alt.Y("Schätzfehler", title="Schätzfehler",scale=alt.Scale(domain=(min_y,max_y)))
    )
    return chart.properties(width=700)


def chart_regression_gd(df, ws):
    df = df.copy(deep=True)
    df["Yhat"] = ws[0] + ws[1]*df["Werbeausgaben"]
    min_x, max_x = df["Werbeausgaben"].min(), df["Werbeausgaben"].max()
    min_y, max_y = -19,20#df.min().min(), df.max().max()
    points = alt.Chart(df).mark_circle(color="#434A56",size=100).encode(
            alt.X("Werbeausgaben",scale=alt.Scale(domain=(0.9*min_x,1.1*max_x))),
            alt.Y("Absatz",scale=alt.Scale(domain=(0.9*min_y,1.1*max_y))
                , title="Absatz"),
            tooltip= [alt.Tooltip(field="Yhat", title="geschätzter Absatz", type="quantitative", format=".2f")]
    )
    line = alt.Chart(df).mark_line(color="#F63366", size=2).encode(
            alt.X("Werbeausgaben"),#,scale=alt.Scale(domain=(0.9*min_x,1.1*max_x))),
            alt.Y("Yhat")#alt.Y("Absatz_Prognose")
    )
    return (points + line).properties(width=700)

###### DATA

def _calc_loss_w1(b0,df):
    'Calculates Loss based on n different w1'
    ws = np.arange(-20,20,0.1)
    x = df["Werbeausgaben"].values
    y = df["Absatz"]
    losses = []
    for w in ws:
        length = len(x)
        loss = (1/2*length) * sum((y - (b0 + w * x) )**2)
        losses.append(loss)
    df = (pd.DataFrame((losses,ws)).T
     .rename({0:"Loss",1:"w1"}, axis=1)
     #.assign(w1=lambda x: x.round(2))
     )
    df["w1"] = df["w1"].round(2)
    return df

def _calc_loss_b0(w1,df):
    'Calculates Loss based on n different b0'
    bs = np.arange(-20,20,0.1)
    x = df["Werbeausgaben"].values
    y = df["Absatz"]
    losses = []
    for b in bs:
        length = len(x)
        loss = (1/2*length) * sum((y - (b + w1 * x) )**2)
        losses.append(loss)
    df = (pd.DataFrame((losses,bs)).T
     .rename({0:"Loss",1:"b0"}, axis=1)
     #.assign(w1=lambda x: x.round(2))
     )
    df["b0"] = df["b0"].round(2)
    return df




###### DATA
def simulate_regression_data(b0=5,w1=1.4,w2=2.1):
    'Generates df with 12 rows based on polynomial function'
    np.random.seed(1023)
    
    monate = ["Januar","Februar","März","April","Mai","Juni"
         ,"Juli","August", "September","Oktober","November","Dezember"]
    n = len(monate)
    x = np.linspace(0.1,2,num=n)
    y_true = np.polynomial.polynomial.polyval(x,[b0,w1,w2]) + np.sin(8*x) + np.random.random(n)#*b0/2
    df = (pd.DataFrame({"y":y_true,"x":x})
            .rename({"x":"Werbeausgaben","y":"Absatz"}, axis=1) # Give x and y specific names
            .assign(Monat_str=monate,
                    Monat_num=range(1,13))
            )
    return df

def df_to_table(df):
    'Returns reduced and formated df for table printing'
    if df["Absatz_Prognose"].sum() == 0:
        df = (df.iloc[:,[0,1]]
                    .applymap("{0:.2f}".format)
                .set_index(df["Monat_str"])
            )
    else:
        df = (df.iloc[:,[0,1,4]]
                    .applymap("{0:.2f}".format)
                .set_index(df["Monat_str"])
            )
    return df





@st.cache
def gradient_descent(b0,w1, df,lr=0.01, epochs=100):
    '''
    X = (n,m), n = observations, m = features (note: include b0 = 1)
    y = (n,1)
    ws = shape (2,1)
    
    See also: https://towardsdatascience.com/gradient-descent-in-python-a0d07285742f
    '''
    print("Calculating")
    m = len(df)
    X = np.concatenate((np.ones((m,1)),df["Werbeausgaben"].values.reshape(-1,1)), axis=1)
    y = df["Absatz"].values.reshape(-1,1)
    ws = np.array((b0,w1)).reshape(-1,1)
    cost_history = np.zeros(epochs)
    ws_history = np.zeros((epochs,2))
    for e in range(epochs):
        yhat = np.dot(X,ws)
        ws = ws - (1/m)*lr * (X.T.dot((yhat - y)))
        ws_history[e,:] = ws.T 
        cost_history[e] = _calc_cost(ws,X,y)
    return ws, cost_history, ws_history


def _calc_cost(ws, X, y):
    m = len(y)
    yhat = X.dot(ws)
    cost = (1/2*m)*np.sum(np.square(y - yhat))
    return cost


@st.cache
def update_df(b0,w1,df):
    df["Absatz_Prognose"] = float(b0) + float(w1) *df["Werbeausgaben"]
    df["Schätzfehler"] = df["Absatz"] - df["Absatz_Prognose"]
    df["Schätzfehler2"] = df["Schätzfehler"]**2
    return df