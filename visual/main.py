import json
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from urllib.request import urlopen
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = dbc.ButtonGroup(
    [
        html.Form(action='https://github.com/cjoshi7/covid19-date-selector',
                  children=dbc.Button('Documentation', color='primary', type='submit')),

        html.Form(action='https://github.com/nytimes/covid-19-data',
                  children=dbc.Button('Download Dataset', color='primary', type='submit'))
    ]
)

jumbotron = dbc.Jumbotron(
    [
        html.H1("COVID-19 Date Selector", className="display-3"),
        html.P(
            "Visualize the spread of the virus on a specific day",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "@cjoshi7",
        ),
        html.P(buttons),
    ]
)

app.layout = html.Div([
    html.Div(jumbotron),
    html.Div(
        dcc.DatePickerSingle(
            id='date',
            min_date_allowed='2020-1-21',
            max_date_allowed='2021-2-5',
            initial_visible_month='2021-2-5',
            date='2021-2-5'
        )
    ),
    html.Div(
        id='picked_date'
    ),
    html.Div(
        [dcc.Graph(id="choropleth")]
    )
    # Include multiple types of graphs for each date.
])

@app.callback(
    Output("choropleth", "figure"), 
    [Input("date", "date")])
def display_choropleth(date):
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    raw_df = pd.read_csv("us-counties.csv",
                    dtype={"fips": str})
    filtered_df = raw_df[raw_df.date == date]

    fig = px.choropleth(filtered_df, geojson=counties, locations='fips', color='cases',
                            color_continuous_scale="Viridis",
                            range_color=(0, filtered_df['cases'].mean() * 1.5),
                            scope="usa",
                            labels={'cases':'infection rate'}
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
