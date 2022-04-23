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

       
firtscol=                    dbc.Col([ 
    dbc.Card(
                    html.H5("50% width card"),style ={ "marginRight" :  "1em", "marginLeft" :  "1em",}
)],width=1)



secondcol =                   dbc.Col([ 
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
            ],className="g-0",)
            ]),
            style ={"borderColor" :"blue"}),

                    ])                   



secondcol2 =                   dbc.Col([ 
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
                   justfigure()
                ], width=4),
            ],className="gx-1 gy-1",)
            ]),
            style ={"borderColor" :"blue"}),

                    ])       
app.layout = html.Div([
                define_header(),

                dbc.Row([
          secondcol,
firtscol,
                ],className="g-0",),

dbc.Row([
          firtscol,
secondcol2,
                ],className="g-0",),
                dbc.Row(secondcol2)
])

                
    

# Run app and display result inline in the notebook

if __name__ == '__main__':
    app.run_server(debug=True)
