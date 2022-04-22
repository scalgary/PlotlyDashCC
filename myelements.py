from dash import Dash, html, dcc


def define_header():
    return html.Div(
        className="app-header",
        children=[
            html.Div('Plotly Dash', className="app-header--title")
        ]
    )
