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
    'Personal': [u'Una relación amorosa', 'Depresión', 'Desempleo'],
    'Familiar': [u'Los hijos', 'Los suegros', 'Otros miembros de la familia'],
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
    html.H4("Seleccione tipo de problema"),
    dcc.RadioItems(id="tipo_problema", options=[{"label":x,"value":x} for x in problemas], value="Personal",
                   labelStyle={
                    'display': 'block',
                    'margin-right': '7px',
                    'font-weight': 500
                }),
    html.Br(),
    html.H4(u"Problema específico"),

    dcc.RadioItems(id='problema_especifico', value="____",
                   labelStyle={
                    'display': 'block',
                    'margin-right': '7px',
                    'font-weight': 500
                }

                   )
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
            dbc.Col(html.H4("Dilemas, Problemas o Conclictos?"), width={"size":6,"offset":3}),

            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(html.Div(id='descripcion_problema'),

                                label= u"Descripción del problema",
                                style= {
                                    'display': 'block',
                                    'margin-right': '7px',
                                    'margin-top': '40px',
                                    'font-size': '2rem'
                                } ),

                dbc.Tab(dcc.Graph(id="plot-active"), label="Proyecto final")
            ])
        ])
    ])
])
#####CALLBACKS


### ACTUALIZAR OPCIONES PARA CADA TIPO DE PROBLEMA
@app.callback(
    Output('problema_especifico', 'options'), #options property is updated here
    Input('tipo_problema', 'value'))
def def_problema_seleccionado(problema_seleccionado):
    return [{'label': i, 'value': i} for i in problemas[problema_seleccionado]]

### DESCRIPCION DEL PROBLEMA
@app.callback(
    Output('descripcion_problema', 'children'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'))
def def_descripcion_problema(ps, pe):
    return u'Usted ha señalado que tiene un problema {} relacionado con  {}'.format(
        ps.lower(), pe.lower(),
    )


if __name__ == '__main__':
    app.run_server(debug=True)