import json
import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from urllib.request import urlopen

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

buttons = dbc.ButtonGroup(
    [
        html.Form(action="https://github.com/cjoshi7/covid19-date-selector",
                  children=dbc.Button("Documentation", color="primary", type="submit")),

        html.Form(action="https://github.com/nytimes/covid-19-data/blob/master/us-counties.csv",
                  children=dbc.Button("Download Dataset", color="primary", type="submit"))
    ]
)

radiobuttons = dcc.RadioItems(
    id="datatype",
    options = [
        {"label": "Infection Rate", "value": "cases"},
        {"label": "Death Rate", "value": "deaths"}
    ],
    value = "cases",
    className="radio",
)

date_selector = dcc.DatePickerSingle(
    id="dateselector",
    min_date_allowed="2020-1-21",
    max_date_allowed="2021-2-5",
    initial_visible_month="2021-2-5",
    date="2021-2-5"
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
    html.Div(date_selector),
    html.Div(radiobuttons),
    html.Div(
        [dcc.Graph(id="choropleth")]
    )
    # Include multiple types of graphs for each date.
])

@app.callback(
    Output("choropleth", "figure"), 
    Input("dateselector", "date"),
    Input("datatype", "value"))
def display_choropleth(date, datatype):

    color = "Viridis"
    label = "Infection Rate"
    if datatype == "deaths":
        color = "hot"
        label = "Death Rate"

    with urlopen("https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json") as response:
        counties = json.load(response)

    raw_df = pd.read_csv("us-counties.csv",
                    dtype={"fips": str})
    filtered_df = raw_df[raw_df.date == date]

    fig = px.choropleth(filtered_df, geojson=counties, locations='fips', color=datatype,
                            color_continuous_scale=color,
                            range_color=(0, filtered_df[datatype].mean() * 1.5),
                            scope="usa",
                            labels={datatype: label}
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
