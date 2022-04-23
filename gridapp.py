import plotly.express as px
import dash

from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

from dash import Dash, html, dcc

from myelements import define_header
from helptest import drawFigure,drawText, justfigure,emptyfigure

# app = dash.Dash(__name__,external_stylesheets=[dbc.themes.PULSE])
from dash import Dash, html



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div("2", style={"height": 80}, className="border gy-4"),
                        html.Div("3", style={"height": 900}, className="border gy-4"),
                    ], 
                    width=3,
                ),
                dbc.Col(html.Div("1", className="vh-100 border")),
            ],
             className="gx-5",
        )
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)