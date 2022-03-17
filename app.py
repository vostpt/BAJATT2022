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

color_map = {
    "WARNING":"#C81D25",
    "AVARIA":"#DE6E4B",
    "ACIDENTE":"#AC9FBB",
    "AVARIA MECÂNICA":"#4F5D75",
    "DESPISTE":"#2D3142",
    "DESISTÊNCIA":"#242424"
}


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # AUTOMATIC UPDATER 
                dcc.Interval(
                    id='interval-component',
                    interval=60*1000, # in milliseconds
                    n_intervals=0
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Row(html.Hr()),
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
                            html.P("CONFIRM by VOST PORTUGAL ")
                        ),
                    ],
                ),
            ], 
        style={"height": "20%", "background-color": "#1D1E2C"},
        ),    
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id='map'), width=2,xs=12, sm=12,md=12,lg=12,xl=4,
                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Card(
                                    [
                                        dbc.CardHeader("TOTAL INCIDENTS", style={"background": "#FF495C","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("TOTAL INCIDENTES", style={"color":"#FF495C"}, className="card-title"),
                                                        html.H4(id="totals"),
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
                                                        html.H4(id="total_warnings"),
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
                                                        html.H4(id="total_breakdowns"),
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
                                        dbc.CardHeader("TOTAL MECHANICAL BREAKDOWNS", style={"background": "#4F5D75","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("AVARIA MECÂNICA", style={"color":"#4F5D75"}, className="card-title"),
                                                        html.H4(id="total_mechs"),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("OFF PISTE", style={"background": "#2D3142","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("DESPISTE", style={"color":"#2D3142"}, className="card-title"),
                                                        html.H4(id="total_outs"),
                                                    ],

                                        ),
                                    ],
                            ),
                            dbc.Card(
                                    [
                                        dbc.CardHeader("OUT OF RACE", style={"background": "#242424","color":"white"}),
                                        dbc.CardBody(
                                                    [
                                                        html.H6("DESISTÊNCIA", style={"color":"#242424"}, className="card-title"),
                                                        html.H4(id="total_offpiste"),
                                                    ],

                                        ),
                                    ],
                            ),
                        ], 
                    ),

                    width=2,xs=12, sm=12,md=12,lg=6,xl=2, 
                ),
                dbc.Col(
                    dbc.Row(dcc.Graph(id='pie')),
                width=3,xs=12, sm=12,md=12,lg=12,xl=3,
                ),

            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(width=4,xs=12, sm=12,md=4,lg=4,xl=4),
                                dbc.Col(
                                    dbc.Row(
                                        [
                                            dbc.Row(dbc.Col(width=12),),
                                            dbc.Row(html.H6("POWERED BY VOST PORTUGAL",style={"align":"center"}),),
                                            dbc.Row(html.H6("VOST PORTUGAL for ACP MOTORSPORTS",style={"align":"center"}),),
                                            dbc.Row(html.H6("CC BY-NC-SA 2022",style={"align":"center"}),),
                                        ],
                                    ),
                                ),
                            ],
                         style={"height": "30%", "background-color": "#242424"},
                        ),
                    ],
                ),
                
            ], 
        style={"height": "30%", "background-color": "#242424"},
        ),    
    ],
    style={"width":"100vw","height": "97vh"},
)


# DEFINE CALL BACKS 

@app.callback(
    Output(component_id="map",component_property="figure"),                           # returns map
    Output(component_id="totals",component_property="children"),                    # returns variable
    Output(component_id="total_warnings",component_property="children"),                     # returns variable
    Output(component_id="total_breakdowns",component_property="children"),                 # returns variable
    Output(component_id="total_mechs",component_property="children"),               # returns variable
    Output(component_id="total_outs",component_property="children"),                             # returns table
    Output(component_id="total_offpiste",component_property="children"),                             # returns table
    Output(component_id="pie",component_property="figure"),  
    Input(component_id="interval-component", component_property="n_intervals"),             # Triggers Call Back based on time update

)


# WHAT HAPPENS WHEN CALL BACK IS TRIGGERED
def confirmUupdate(value):

    # DATA TREATMENT


    df_ss1_cc = pd.read_csv('ss1_cc.csv')


    df_live_incidents = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT5ZYA_C5ziVBuAAhRI0LKOMSjkpr2A157Q_WNENhgFVsivnRil4Au3lXE0r_QOg1RnE5HRcN_k29Ej/pub?gid=1319524241&single=true&output=csv')
    df_live_cc = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT5ZYA_C5ziVBuAAhRI0LKOMSjkpr2A157Q_WNENhgFVsivnRil4Au3lXE0r_QOg1RnE5HRcN_k29Ej/pub?gid=89946936&single=true&output=csv')



    totals = str(round(df_live_incidents['total_incidents'].sum()))

    total_warnings = df_live_incidents.loc[df_live_incidents['type'] == "WARNING", 'total_incidents'].sum()

    total_breakdowns = df_live_incidents.loc[df_live_incidents['type'] == "AVARIA", 'total_incidents'].sum()

    total_mech = df_live_incidents.loc[df_live_incidents['type'] == "AVARIA MECÂNICA", 'total_incidents'].sum()

    total_out = df_live_incidents.loc[df_live_incidents['type'] == "DESPISTE", 'total_incidents'].sum()

    total_gaveup = df_live_incidents.loc[df_live_incidents['type'] == "DESISTÊNCIA", 'total_incidents'].sum()


    fig = px.scatter_mapbox(df_live_cc, lat="lat", lon="lon", size='reports',hover_name="reporter", hover_data=["reports"],
                            color_discrete_sequence=["red"], zoom=8)
    fig.update_layout(mapbox_style="carto-darkmatter")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    pie_chart = px.pie(df_live_incidents,names='type',values='total_incidents',hole=0.6,color='type',color_discrete_map=color_map)


    return fig, totals, total_warnings, total_breakdowns, total_mech, total_out, total_gaveup, pie_chart



# -------------------------------------------------------------------------------------
# --------------------------------  START THE APP -------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8081, debug=False)

# -------------------------------------------------------------------------------------
# --------------------------------  THE END       -------------------------------------
# -------------------------------------------------------------------------------------
