from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import plotly.express as px
import csv
import base64
import datetime
import io

import pandas as pd


app = Dash(__name__)

dates = []
sales = []
region = []
with open('data processing/filtered_data.csv') as csv_file:
    csvreader = csv.reader(csv_file)
    counter = 0
    for row in csvreader:
        if (counter == 0):
            counter += 1
            continue
        else:
            dates.append(row[1])
            sales.append(row[0])
            region.append(row[2])
df = pd.DataFrame(dict(
    Dates=[*dates],
    Sales=[*sales],
    Region=[*region]))

colors = {
    'background': '#000000',
    'text': '#FFFFFF',
    'font-family': 'arial',
    'padding-top': '30px',

}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Pink Morsel Sales over Time',
            style={'textAlign': 'center',
                   'color': colors['text'],
                   'font-family': colors['font-family'], 'margin-top': colors['padding-top']}),
    html.H4(children='A visualization of Pink Morsel\'s sales over the last few years', style={
        'textAlign': 'center',
        'color': colors['text'], 'font-family': colors['font-family'], 'margin-top': colors['padding-top']
    }),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        style={'color': colors['text'], 'font-family': colors['font-family']},
        id="checklist",
        options=["north", "east", "south", "west", "all"],
        value=["north"],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"),
    Input("checklist", "value"))
def update_line_chart(regions):

    if ('all' in regions):
        fig = px.line(df, x="Dates", y="Sales", color="Region")
    else:
        filtered_df = df.loc[df['Region'].isin(regions)]
        fig = px.line(filtered_df, x="Dates", y="Sales", color="Region")
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig


app.run_server(debug=True)
