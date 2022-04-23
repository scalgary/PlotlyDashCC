
import plotly.express as px
import dash
import plotly.graph_objects as go

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from dash import Dash, html, dcc
import pandas as pd

# Iris bar figure
# Data
df = px.data.iris()
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(
                        df, x="sepal_width", y="sepal_length", color="species"
                    ).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)',
                        margin=go.layout.Margin(
                        l=0, #left margin
                        r=0, #right margin
                        b=0, #bottom margin
                        t=0, #top margin
                    )),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# Text field
def drawText():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Text"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])

# Data


def justfigure():
    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure= px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
                )
            ])
    ),  
    ],)



def emptyfigure():
    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
    return  html.Div([
        dbc.Card(
            dbc.CardBody([]),style={'borderColor': "green"}),])
    


#style={'backgroundColor': "blue"}