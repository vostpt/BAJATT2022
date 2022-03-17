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





# -----------------------------------------------
#              APP STARTS HERE
# -----------------------------------------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='CONFIRM - SK4U', update_title=None,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=0.7, minimum-scale=0.4"}],
                )

server = app.server

CONFIRM_LOGO = app.get_asset_url('CONFIRM_Logotype.png')

# DATA TREATMENT


df_ss1_cc = pd.read_csv('ss1_cc.csv')



df_live = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSlasVmsQglAUGhesSL9_bJHaZ4rsbNG0m2U5nTFj25LyBdylAPiRvt2eDIVjfFQ7yI_ElWDus-qx2b/pub?gid=509896708&single=true&output=csv')


total_incidents = str(round(df_live['INCIDENT SUM'].sum()))

total_warnings = df_live.loc[df_live['INCIDENT UNIQUE'] == "WARNING", 'INCIDENT SUM'].sum()

total_breakdowns = df_live.loc[df_live['INCIDENT UNIQUE'] == "Avaria", 'INCIDENT SUM'].sum()

total_mech = df_live.loc[df_live['INCIDENT UNIQUE'] == "Avaria Mecânica", 'INCIDENT SUM'].sum()

total_out = df_live.loc[df_live['INCIDENT UNIQUE'] == "Despiste", 'INCIDENT SUM'].sum()

total_gaveup = df_live.loc[df_live['INCIDENT UNIQUE'] == "Desistência", 'INCIDENT SUM'].sum()


fig = px.scatter_mapbox(df_ss1_cc, lat="lat", lon="lon", hover_name="Name", hover_data=["Description"],
                        color_discrete_sequence=["red"], zoom=8)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(width=2,xs=12, sm=12,md=1,lg=1,xl=1),
                                dbc.Col(html.H3("BAJA TT 2022"),width=4,xs=12, sm=12,md=4,lg=4,xl=4),
                                dbc.Col(width=4,xs=12, sm=12,md=1,lg=4,xl=4),
                                dbc.Col(html.Img(src=CONFIRM_LOGO, height="37px"),width=2,xs=12, sm=12,md=1,lg=1,xl=1),  # CONFIRM LOGO - DO NOT REMOVE
                            ],
                        ),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(width=2,xs=12, sm=12,md=1,lg=2,xl=1),
                        dbc.Col(
                            html.H5("by VOST PORTUGAL ")
                        ),
                    ],
                ),
            ], 
        style={"height": "20%", "background-color": "#242424"},
        ),    
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='map',figure=fig), width=2,xs=12, sm=12,md=12,lg=12,xl=4,
                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Card(
                                    [
                                        dbc.CardHeader("TOTAL INCIDENTS", style={"background": "#FF495C","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("TOTAL ACIDENTES", style={"color":"#FF495C"}, className="card-title"),
                                                        html.H4(id="total_incidents",children=total_incidents),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("TOTAL WARNINGS", style={"background": "#C81D25","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("RACE DIRECTOR", style={"color":"#C81D25"}, className="card-title"),
                                                        html.H4(id="total_warnings",children=total_warnings),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("BREAKDOWNS", style={"background": "#DE6E4B","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("AVARIAS", style={"color":"#DE6E4B"}, className="card-title"),
                                                        html.H4(id="total_breakdowns",children=total_breakdowns),
                                                    ],

                                        ),
                                    ],
                            ),
                        ], 
                    ),

                    width=2,xs=12, sm=12,md=12,lg=6,xl=2, 
                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Card(
                                    [
                                        dbc.CardHeader("TOTAL MECHANICAL BREAKDOWNS", style={"background": "#FF495C","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("AVARIA MECÂNICA", style={"color":"#FF495C"}, className="card-title"),
                                                        html.H4(id="total_mechs",children=total_mech),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("OFF PISTE", style={"background": "#C81D25","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("Despiste", style={"color":"#C81D25"}, className="card-title"),
                                                        html.H4(id="total_outs",children=total_out),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("OUT OF RACE", style={"background": "#DE6E4B","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("DESISTÊNCIA", style={"color":"#DE6E4B"}, className="card-title"),
                                                        html.H4(id="total_offpiste",children=total_gaveup),
                                                    ],

                                        ),
                                    ],
                            ),
                        ], 
                    ),

                    width=2,xs=12, sm=12,md=12,lg=6,xl=2, 
                ),

            ],
        ),
    ],
    style={"width":"100vw","height": "97vh"},
)

# TEST DATAFRAME



# -------------------------------------------------------------------------------------
# --------------------------------  START THE APP -------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8081, debug=True)

# -------------------------------------------------------------------------------------
# --------------------------------  THE END       -------------------------------------
# -------------------------------------------------------------------------------------
