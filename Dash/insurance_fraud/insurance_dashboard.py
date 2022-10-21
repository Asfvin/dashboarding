import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px


app = Dash(__name__)

file = 'data\Train_Demographics.csv'

df = pd.read_csv(file)

fig = px.bar(df, x="InsuredAge", y='InsuredGender', color="InsuredEducationLevel", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Sample Insurance Dashboard'),
    html.Br,
    dcc.Graph(
        id='gender',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
