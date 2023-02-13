import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import json

# df_pt1 = pd.read_csv(r"c:\Users\{user}\Downloads\HIST_PAINEL_COVIDBR_2021_Parte1_21dez2021.csv", sep=";")
# df_pt2 = pd.read_csv(r"c:\Users\{user}\Downloads\HIST_PAINEL_COVIDBR_2021_Parte2_21dez2021.csv", sep=";")
# df_complete = pd.concat([df_pt1, df_pt2])
# df_states = df_complete[(~df_complete["estado"].isna()) & (df_complete["codmun"].isna())]
# df_brasil = df_complete[df_complete["regiao"] == "Brasil"]
# df_states.to_csv("df_states.csv")
# df_brasil.to_csv("df_brasil.csv")

df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

df_states_ = df_states[df_states["data"]]

brazil_states = json.load(open("/brazil_geo.json", "r"))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

fig = px.choropleth_mapbox(df_states_, locations="estado", color="casosNovos",
                           center={"lat": -22.8573, "lon": -47.2211},
                           geojson=brazil_states, color_continuous_scale="Redor", opacity=0.4,
                           hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estados": True})