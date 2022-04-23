
import plotly.express as px
import dash

from jupyter_dash import JupyterDash
#import dash_core_components as dcc
#import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from dash import Dash, html, dcc

app_header = html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    )
# Iris bar figure
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
                    ),
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
df = px.data.iris()

# Build App
#app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.PULSE])
import dash_bootstrap_components as dbc
from dash import html

baby =        dbc.Card(
            dbc.CardBody([
                
                    html.H5("50% width card", className="card-title"),
                    html.P(
                        [
                            "This card uses the ",
                            html.Code("w-50"),
                            " class to set the width to 50%",
                        ],
                        className="card-text",
                    ),
                ]
            ,style ={"color" : "blue", "paddingLeft":"2em"})
        )
cards = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("75% width card", className="card-title"),
                    html.P(
                        [
                            "This card uses the ",
                            html.Code("w-75"),
                            " class to set the width to 75%",
                        ],
                        className="card-text",
                    ),
                ]
            ),
            className="w-75 mb-3",
        ),
        dbc.Row([
            dbc.Col([
       baby, 
    ],style={"paddingRight" :"1em", "paddingLeft" : "1em"}, width=6
  ),
 dbc.Col([
       baby,
    ],style={"paddingRight" :"1em","paddingLeft" : "1em"}, width=6)
])])


app_header = html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    )
app.layout = html.Div([
                app_header,
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=4),
                dbc.Col([
                   drawFigure()
                ], width=4),
                dbc.Col([
                   drawFigure()
                ], width=4),
            ], align='center')])), 
            cards])
# Run app and display result inline in the notebook

if __name__ == '__main__':
    app.run_server(debug=True)