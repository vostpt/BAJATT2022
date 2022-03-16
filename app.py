# -*- coding: utf-8 -*-
# Original Code by Jorge Gomes for VOST Portugal

# -----------------------------------------------
#                  LIBRARIES
# -----------------------------------------------


# Import Dash and Dash Bootstrap Components
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
# Import Core Libraries
import pandas as pd
import plotly.express as px
import geopandas 




# -----------------------------------------------
#              APP STARTS HERE
# -----------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='CONFIRM - SK4U', update_title=None,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=0.7, minimum-scale=0.4"}],
                )

server = app.server

app.layout = dbc.Container(
    [
    dbc.Row(dbc.Col(html.H1("THIS WILL BE AWESOME"))),
    dbc.Row(dbc.Col(html.H5("OH YEAH"))),
    ]
)

# -------------------------------------------------------------------------------------
# --------------------------------  START THE APP -------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True)