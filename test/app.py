import plotly.express as px
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.PULSE])
# Data
df = px.data.iris()
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

app_header = html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    )
app.layout = html.Div([
                app_header,
                dbc.Row([
                    dbc.Col([
                    drawFigure() 
                    ], width=3),
                    dbc.Col([
                    drawFigure()
                    ], width=3),
                    dbc.Col([
                    drawFigure() 
                   ], width=6),
            ], align='center')
])

# Run app and display result inline in the notebook

if __name__ == '__main__':
    app.run_server(debug=True)

