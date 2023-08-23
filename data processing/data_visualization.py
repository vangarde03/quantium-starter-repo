# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import csv

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
dates = []
sales = []
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


df = pd.DataFrame(dict(
    Dates=[*dates],
    Sales=[*sales]
))
fig = px.line(df, x="Dates", y="Sales",
              title="Pink Morsel Sales over Time Chart")
fig.show()
