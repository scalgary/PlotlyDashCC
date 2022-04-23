import dash
import dash_bootstrap_components as dbc
from dash import html


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.PULSE])


first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This card also has some text content and not much else, but "
                "it is twice as wide as the first card."
            ),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
)


cards = dbc.Row(
    [
        dbc.Col(first_card, width=4),
        dbc.Col(second_card, width=8),
    ]
)


app.layout=cards
if __name__ == '__main__':
    app.run_server(debug=True)