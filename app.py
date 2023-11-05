# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("Quantium Task 2.csv")

fig = px.line(df, x='date', y='Sales', title='Sales Over Time')

app.layout = html.Div(children=[
    html.H1(children='Price of Pink Morsel Over Time'),

    html.Div(children='''
        Line graph shows Date vs Price of Pink Morsel.
             Sales are higher after the price was increased.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
