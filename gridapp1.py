import plotly.express as px
import dash

from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from dash import Dash, html, dcc

from myelements import define_header
from helptest import drawFigure,drawText, justfigure,emptyfigure

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.PULSE])


app.layout = html.Div([
                define_header(),
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
 dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=4),
                dbc.Col([
                 emptyfigure()
                ], width=4),
                dbc.Col([
                   justfigure()
                ], width=4),
            ])]),style ={"borderColor" :"blue"}),

dbc.Col([ 
    html.H5("50% width card"),
    
    ],style={
        'textAlign': 'center',
        'border': '1px solid red',
    }),
 dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawFigure()
                ], width=4,),
                dbc.Col([
                   drawFigure()
                ], width=8),
            ])
            ]),style ={"borderColor" :"purple"}),


            ])




# Run app and display result inline in the notebook

if __name__ == '__main__':
    app.run_server(debug=True)
