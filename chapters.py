import streamlit as st
from sthelper import print
from linear_regression import *

def show_not_implemented():
    st.error("Kapitel noch nicht verfügbar")
    

def show_ch1():
    'Includes "view" of first chapter'

    st.title(":star: Wie lernen Maschinen? ")
    text = f"Um zu verstehen, was 'Lernen' in Maschinelles Lernen bedeutet, soll die folgende Fallstudie unterstützen eine Intuition für den Lernprozess zu entwickeln."
    p = print(text,"justify")

    st.subheader("Absatzprognose der Fashion GmbH")
    text = """
    Nikolas Waltherschmied ist seit 4 Jahren Geschäftsführer und Gründer der Fashion GmbH, einem Online-Versandhändler für Modeartikel. Nikolas ist unzufrieden mit den Entwicklungen in den letzten Monaten. Zwar wächst die Fashion GmbH weiter zweistellig, jedoch steigen die Kosten überproportional, so dass die Profitabilitätsentwicklung nicht mehr mit den Erwartungen Schritt halten kann.  
    """ 
    p = print(text,"justify", False)

    text = "Ein eigens für die Analyse der Kostenentwicklung aufgestelltes Projekt ('Fashion4Future') hat eine Vielzahl von Faktoren ausgemacht. Ein Faktor, der Nikolas ganz besonders stört, ist die gestiegene Stornierungsquote. Immer mehr Kunden stornieren ihre Bestellungen noch bevor die Ware geliefert wurde (anders als bei Rücksendungen). Diese führt nicht nur auf der Kostenseite zu Problemen, sondern ist auch ärgerlich, weil vermeintlich gemachter Umsatz wieder wegfällt. Hohe Kosten entstehen insbesondere dadurch, dass oftmals der gesamte Waren- und Logistikprozess angestoßen wird (z.B. Ware im Lager suchen, Bestellvorgänge bei Lieferanten auslösen, Ware verpacken etc.)."""
    p = print(text, "justify")
    
    text = "Um den Grund für die steigenden Stornierungsquoten zu verstehen, hat das Projektteam eine Vielzahl von Analysen angestoßen und Kundenbefragungen durchgeführt. Gesamtfazit der Analysen:"
    p = print(text, "justify")

    p = st.markdown("""
    - Stornierungen entstehen dann, wenn Kunden lange **Lieferzeiten** avisiert werden (mehr als 3 Tage) und sie deshalb zu konkurrierenden Versandhändlern wechseln, die schneller liefern können 
    
    - Lange Lieferzeiten entstehen durch **schlechte Absatzprognosen**, die dazu führen, dass die Lager nicht ausreichend gefüllt sind  
    
    - Wichtigster Treiber für den Absatz ist der **Werbeaufwand**: wird viel Geld für Werbung ausgegeben, steigt der Absatz und vice versa
    
    """)

    text = "Kurzum: könnte man den zukünftigen Absatz besser prognostizieren, wäre die Lager 'optimal' gefüllt und die Lieferzeiten könnten minimiert werden."
    p = print(text,"justify")

    p = print(text, "justify")

    text = "Norbert Bauchschätzer, Leiter Controlling, wird deshalb damit beauftragt die Absatzprognose zu verbessern und durch eine computerbasierte Prognose zu ergänzen"
    p = st.markdown(f"""
    > :bulb: **Aufgabe:**  
    > {text}
    """)


def show_ch2():
    'Includes "view" of second chapter'
    #st.sidebar.subheader("Auswahl")
    #w0 = st.sidebar.slider("w0")
    #w1 = st.sidebar.slider("w1")
    
    text = """Dieser erlernte Zusammenhang ("Regeln") kann dann auf neue, unbekannte Eingangsdaten angewandt werden, um Antworten zu prognostizieren. 
    ein System trainiert und nicht explizit programmiert. 
    Maschinelles Lernen bezweckt die Generierung von »Wissen« aus »Erfahrung«, indem Lernalgorithmen aus Bei- spielen ein komplexes Modell entwickeln. Das Modell, und damit die automatisch erworbene Wissensrepräsentation, kann anschließend auf neue, potenziell unbekannte Daten derselben Art angewendet werden.
    """

    st.title(":star: Grundlagen des Überwachten Lernen")
    st.markdown("### Einleitung")
    text = """
    Der Mensch lernt aus Erfahrung. Das (überwachte) Maschinelle Lernen bezweckt die Generierung von 'Wissen' ebenfalls aus 'Erfahrung'. 
    Der Computer erlernt mittels eines Lernalgorithmus einen Zusammenhang ("Regeln") zwischen Eingabedaten ("Daten") und dazu passenden, gekennzeichneten Daten ("Antworten"). Dem Computer werden demnach Regeln zur Prognose nicht explizit vorgegeben, sondern er ermittelt diese mittels Beispieldaten. Dieses Vorgehen wird auch 'Training' bezeichnet.
    """
    p = print(text,"justify", False)
    st.image("assets/ML1.png",caption="Abbildung 1: Training mittels Eingabe- und Antwortdaten",use_column_width=True)

    text = """Der im Training ermittelte Zusammenhang ("Regeln") kann dann auf neue, unbekannte Eingangsdaten angewandt werden, um Antworten zu prognostizieren. """
    p = print(text)
    st.image("assets/ML2.png",caption="Abbildung 2: Prognose mittels neuer Eingabedaten",use_column_width=True)
    print("")    

    
    st.markdown("""
    > ### Übertragung auf die Fashion GmbH")
    > Herr Bauchschätzer die Prognose der Absatzzahlen verbessern. Das Projektteam hat bereits Vorarbeit geleistet und analysiert, dass der Absatz stark abhängig ist vom getätigten Werbeaufwand.
    Man kann den Sachverhalt als 'Überwachtes Lernen'-Problem formulieren:   
    > - Daten: Werbeaufwand
    > - Antworten: Absatzzahlen
    > - Regeln: Zusammenhang zwischen Werbeaufwand und Absatzzahlen
    """)


    st.markdown("### Arten des Überwachten Lernens")

    text = """
    Das Lernen dieser Regeln kann beim Überwachten Lernen grundsätzlich auf **zwei Arten** erfolgen:

    1. parametrisiertes Lernen
    2. nicht-parametrisiertes Lernen
    """
    p = st.markdown(text)
    text = """Bei parametrisierten Lernen bestimmt der Lernalgorithmus feste Parameter, die den Zusammenhang zwischen Eingangs- und Antwortdaten beschreiben. Beim nicht-parametrisierten Lernen wird der Zusammenhang aus den Daten selber erlernt.
    """
    p = print(text)
    print("")
    st.markdown("""**Im weiteren Verlauf der Fallstudie fokussieren wir uns auf das parametrisierte Lernen**.""")
    st.markdown("### Schritte des Überwachten Lernens")
    text = """
    Damit Computer lernen, muss demnach ein (parametrisiertes) Modell trainiert werden. 
    
    Dazu muss zunächst eine Modellstrukutur vorgegeben werden (z.B. Art und Anzahl der Parameter).
    
    Das eigentliche Training erfolgt dann in **drei Schritten**: 

    1. **Vorhersagen:** Modell mit aktuellen Parametern zur Ableitung von Prognosewerten nutzen  
    2. **Vergleichen:** Prognosewerte mit tatsächlichen Werten des Trainingsdatensatezs abgleichen
    3. **Verbessern:** Parameter des Modells anpassen

    Diese Schritte werden so oft wiederholt bis die Prognose zufriedenstellende Ergebnisse liefert.

    """
    p = st.markdown(text)
    st.image("assets/Lernprozess.png",caption="Abbildung 3: Lernprozess",use_column_width=True)

def show_ch3():
    st.sidebar.subheader("Wähle Lernschritt aus")
    st.sidebar.radio("", ["Schritt 1: Vorhersagen","Schritt 2: Vergleichn", "Schritt 3: Verbessern"])
    st.sidebar.subheader("Wähle Parameter")
    show_line = st.sidebar.checkbox("Gerade anzeigen", value=False)
    show_error = st.sidebar.checkbox("Abweichung anzeigen", value=False)
    w0 = st.sidebar.slider("Achsenabschnitt (w0)", 0.0, 10.0,value=0.0, step=0.3)
    w1 = st.sidebar.slider("Steigung (w1)", 0.0,10.0,value=0.0,step=0.3)
    update_grid = st.sidebar.checkbox("Aktualisiere Grid?", value=False)
    ### Load Data (small data set - no problem)
    df = load_regression_data(12)
    
    st.title(":star: Lineare Regression")
    st.markdown("""
    ## 1 | Definition einer Modellstruktur

    Wie im vorangegangenen Kapitel dargestellt, benötigt der Computer zunächst eine Modellstruktur zum lernen. 

    Ein einfaches und sehr bekanntes Modell ist das folgende:
    """)

    st.latex(r"y = w_0 + w_1x")

    st.markdown(r"""
    Diese sogenannte univariate lineare Funktion (eine Gerade!) mit zwei Parametern $w_0$ und $w_1$ stellt einen Zusammenhang zwischen den Eingabedaten ($x$) und den Ausgabedaten ($y$) her.
    
    > ### Anwendung auf die Fashion GmbH
    > $\text{Absatz} = w_0 + w_1 \times \text{Werbung}$
    >
    > - $w_0$ = Grundabsatz unabhängig von Werbung (z.B. wiederkehrende Kunden)  
    > - $w_1$ = Effekt der Werbung auf den Absatz
    
    Ziel des Lernalgorithmus ist es nun die Parameter ($w_0$ und $w_1$) so zu ändern, dass der Zusammenhang zwischen $x$ (hier: Werbeaufwand) und $y$ (hier: Absatz) möglichst gut beschrieben wird.


    ## 2 | Beispieldaten (Trainingsdaten)

    Da ein Computer mittels Beispieldaten lernt, wird ein sogenannter **Trainingsdatensatz** benötigt. Herr Bauchschäzter hat einen seinen Mitarbeiter deshalb gebeten die **Zahlen der letzten 12 Monate für Absatz und Werbeaufwand** zusammenzutragen und nach Werbeaufwand zu sortieren. 
    """)
    show_data = st.checkbox("Tabelle anzeigen",value=False)
    data_table = st.empty()#st.table(df)

    st.markdown("""
    ## 3 | Training (Lernen am Beispiel)
    
    Das eigentliche Training erfolgt nun in **drei Schritten**: 

    1. Prognose 
    2. Abgleich Prognose mit tatsächlichen Werten
    3. Anpassung der Parameter

    Wiederhole Schritte 1 bis 3 bis das Ergebnis zufriedenstellend ist.


    ### 3a | Manuelle Suche nach optimalem Parameter
    """)
    print("")

    st.markdown("""#### 1. Prognose """)
    print("")
    print("")

    st.markdown

    df = update_df(w0,w1,df, show_line)
    if show_data:
        data_table.table(df_to_table(df))
    
    
    chart_msg = st.empty()
    chart1 = st.empty()
    show_regression(df, show_line, show_error, chart1, chart_msg)

    st.markdown("#### 2. Abgleich Prognose mit tatsächlichen Werten")
    print("")
    chart2 = st.empty()
    show_y_yhat(df, show_line, show_error, chart2)

    st.markdown("#### 3. Anpassung Parameter")
    print("")
    chart_loss_w1 = plot_loss_w1(df,w0, w1).properties(width=300)
    chart_loss_w0 = plot_loss_w0(df,w0, w1).properties(width=300)
    st.altair_chart(chart_loss_w0 | chart_loss_w1 )

    if update_grid:
        alpha,beta,losses = make_meshgrid(df)
        data = make_df(alpha,beta,losses)
        chart = plot_heatmap(data, w0,w1)
        st.altair_chart(chart)










##placeholder_chart = st.empty()
##placeholder_text = st.empty()
##
###idx = np.argmin(df["loss"])
###df_minimum = df.iloc[[idx]]
##btn = st.sidebar.button("Start search")
##if btn:
##    for idx in np.arange(0,2000,50):
##
##        #idx = st.sidebar.slider("Choose row",min_value=0, max_value=len(df)-1, step=1)
##        df_show = df.iloc[[idx]]
##        values = df_show.values[0]
##        point = alt.Chart(df_show).mark_square(size=100,color="red", opacity=1).encode(
##                alt.X("w"), 
##                alt.Y("b"),
##                tooltip="loss"
##        )   
##
##        chart = (contour + point).properties(width=750, height=750)
##        placeholder_chart.altair_chart(chart)
##        placeholder_text.markdown(f"""Step {idx} of 2000. b0 = {values[0]:.2f}
##                    , w1 = {values[1]:.2f}, loss = {values[2]:.2f}""")
##    
##    
    st.write(fr"""> Modell für Absatzprognose: **$f(Werbung)$** = **`{w0:.2f}`** + **`{w1:.2f}`** $\times$ **$Werbung$**  
    > Durchschnittliche absolute Abweichung: **`{np.sum((df['Absatz']-df['Prognose'])**2)*(1/(2*df.shape[0])):.2f}`**
    """)

    st.markdown("### 3b | Automatische Suche nach optimalen Parametern ")
    #st.altair_chart(right_hand)
    #chart = chart.properties(width=700)
    #if show_error is not None    
    
   
