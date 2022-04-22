import plotly.express as px
import dash

from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from dash import Dash, html, dcc

from myelements import define_header
from helptest import drawFigure,drawText

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
                  dcc.Markdown('''
   ![babies](static/img/babies.png)
''')
                ], width=4),
                dbc.Col([
                   drawFigure()
                ], width=4),
            ], align='center')])), 
            ])




# Run app and display result inline in the notebook

if __name__ == '__main__':
    app.run_server(debug=True)
