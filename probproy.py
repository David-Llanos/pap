import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_table
import pandas as pd
import plotly.graph_objects as go
import numpy as np

import dash_bootstrap_components as dbc

from settings import config, about

external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])

problemas = {
    'Personal': [u'Relación amorosa', 'Depresión', 'Desempleo'],
    'Familiar': [u'Relación con los Hijos', 'Relación con suegros', 'Otros miembros de la familia'], #note unicode for Montréal
    'Laboral': [u'Desmotivación', 'Demasiada presión', 'Falta de oportunidades de crecimiento'] 
}

# App Instance
app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.CERULEAN, config.fontawesome])
app.title = config.name


# Navbar
navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("How it works"), dbc.PopoverBody(about.txt)
        ])
    ])),
    ## links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"), "  Contacts"], href=config.contacts, target="_blank"), 
        dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank")
    ])
])

# Input
inputs = dbc.FormGroup([
    html.H4("Selecciones Tipo de Problema"),
    dcc.Dropdown(id="country", options=[{"label":x,"value":x} for x in problemas], value="Personal")
])
# App Layout
app.layout = dbc.Container(fluid=True, children=[
    ## Top
    html.H1(config.name, id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    ## Body
    dbc.Row([
        ### input + panel
        dbc.Col(md=3, children=[
            inputs, 
            html.Br(),html.Br(),html.Br(),
            html.Div(id="output-panel")
        ]),
        ### plots
        dbc.Col(md=9, children=[
            dbc.Col(html.H4("Forecast 30 days from today"), width={"size":6,"offset":3}), 
            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(dcc.Graph(id="plot-total"), label="Total cases"),
                dbc.Tab(dcc.Graph(id="plot-active"), label="Active cases")
            ])
        ])
    ])
])
'''
@app.callback(
    Output('tipo-radio', 'options'), #options property is updated here 
    Input('lista_problemas', 'value'))
def definir_tipo_problemas(problema_seleccionado):
    return [{'label': i, 'value': i} for i in problemas[problema_seleccionado]]


@app.callback(
    Output('tipo-radio', 'value'),
    Input('tipo-radio', 'options'))
def definir_problema_especifico(opciones_disponibles):
    return opciones_disponibles[0]['value'] #selected value in the RadioItems


@app.callback(
    Output('display-selected-values', 'children'),
    Input('lista_problemas', 'value'),
    Input('tipo-radio', 'value'))
def set_display_children(problema_seleccionado, tipo_seleccionado):
    return u'{} is a city in {}'.format(
        problema_seleccionado, tipo_seleccionado,
    )
'''

if __name__ == '__main__':
    app.run_server(debug=True)