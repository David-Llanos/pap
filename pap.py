import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.H5 import H5

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

# Inputs
inputs = dbc.FormGroup([

    html.H5("1. Seleccione tipo de problema"),
    dcc.RadioItems(id="tipo_problema", options=[{"label":x,"value":x} for x in problemas], value="",
                   labelStyle={'display': 'block'}),

    html.Br(),
    html.H5(u"2. Problema específico", id= 'titulo_problema_especifico', style={'display':'none'}),
    dcc.RadioItems(id='problema_especifico', value="",
                   labelStyle={'display': 'none'}
                   ),
    html.Br(),
    html.H5(u"3. Está usted en una encrucijada donde tiene que tomar decisiones excluyentes?", id= 'titulo_decision_excluyente', style={'display':'none'}),
    dcc.RadioItems(id='decision_excluyente', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                   labelStyle={'display': 'block'}

                   ),

    html.Br(),
    html.H5(u"4a. Es esta una decisión que afecta sus principios y valores?", id= 'titulo_decision_afecta_valores', style={'display':'none'}),
    dcc.RadioItems(id='decision_afecta_valores', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),

    html.Br(),
    html.H5(u"4b. Es difícil identificar sus objetivos y cómo alcanzarlos?", id= 'titulo_objetivo_dificil', style={'display':'none'}),
    dcc.RadioItems(id='objetivo_dificil', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),



])
### CONTENIDOS TAB

# App Layout
app.layout = dbc.Container(fluid=True, children=[
    ## Top
    html.H1(config.name, id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    ## Body
    dbc.Row([
        ### input + panel
        dbc.Col(md=4, children=[
            inputs,
            html.Br(),html.Br(),html.Br(),
            html.Div(id="output-panel")
        ]),
        ### plots
        dbc.Col(md=8, children=[
            dbc.Col(html.H4("Dilemas, Problemas o Conclictos?"), width={"size":6,"offset":3}),

            dbc.Tabs(className="nav nav-pills", children=[
                dbc.Tab(
                    html.Div
                        (id='descripcion_problema'),
                        label= u"Descripción del problema",
                                style= {
                                    'display': 'block',
                                    'margin-right': '7px',
                                    'margin-top': '40px',
                                    'font-size': '2rem'
                                    }
                                ) ,
                                dcc.Textarea(
                                            id='diagnostico',
                                            value='',
                                            style={'display':'none'},
                                        ),
                                        html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'}),

                    dbc.Tab(dcc.Graph(id="proyecto_final"), label="Proyecto final")
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

### OPCIONES DISPONIBLES
""" @app.callback(
    Output('problema_especifico', 'value'),
    Input('problema_especifico', 'options'))
def def_problemas_disponibles(opciones_disponibles):
    return opciones_disponibles['value'] #selected value in the RadioItems """

### OCULTAR/MOSTRAR PREGUNTA SOBRE PROBLEMA ESPECIFICO
@app.callback(
    Output('problema_especifico', 'value'),
    Output('problema_especifico', 'labelStyle'),
    Output('titulo_problema_especifico', 'style'),
    [Input('tipo_problema', 'value')])
def def_mostrar_prob_especifico(tp):
    if tp != '' :
        return ['', {'display': 'block'}, {'display': 'block'}]
    if tp == '':
        return ['',{'display': 'none'}, {'display': 'none'}]

### OCULTAR/MOSTRAR PREGUNTA SOBRE DECISION EXCLUYENTE
@app.callback(
    Output('decision_excluyente', 'value'),
    Output('decision_excluyente', 'labelStyle'),
    Output('titulo_decision_excluyente', 'style'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value')
    )
def def_mostrar_decision_excluyente(tp, pe): #tp: tipo de problema; de : decision excluyente
    if tp != '' and pe != '':
        return ['',{'display': 'block'}, {'display': 'block'}]
    else:
        return ['',{'display': 'none'}, {'display': 'none'}]


### DECIDIR QUE PREGUNTA VALORES U OBJETIVO DEPENDIENDO DE EXCLUYENTE
@app.callback(
    Output('titulo_decision_afecta_valores', 'style'),
    Output('decision_afecta_valores', 'labelStyle'),
    Output('titulo_objetivo_dificil', 'style'),
    Output('objetivo_dificil', 'labelStyle'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('decision_excluyente', 'value')
    )
def def_mostrar_valores_objetivo(tp, pe, de):
    if tp == '' or pe == '' or de == '':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    if de == 'si':
        return {'display': 'block'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}
    if de == 'no':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'block'}



### DIAGNOSTICO
@app.callback(
    Output('diagnostico', 'style'),
    Output('diagnostico', 'value'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('decision_excluyente', 'value'),
    Input('decision_afecta_valores', 'value')
    )
def def_diagnostico(tp, pe, de, av):
    print (tp, pe, de, av)
    if tp != '' and pe != ''and de == 'si' and av== 'si':
        return {'display': 'block','width': '100%', 'height': 100, 'font-size': '2rem' }, u'Usted está enfrentando un\nDilema'
    elif tp != '' and pe != ''or de == 'no' or av== 'no':
        return {'display': 'none','width': '100%', 'height': 100, 'font-size': '2rem' }, u''

### DESCRIPCION DEL PROBLEMA
@app.callback(
    Output('descripcion_problema', 'children'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('decision_excluyente', 'value')
    #Input('decision_afecta_valores', 'value'),
    )
def def_descripcion_problema(tp, pe, de):
    if tp != '' and pe != '' and de != '':
        return u'Usted ha señalado que tiene un problema {} relacionado con  {}. El problema  {} lo(a) obliga a tomar decisiones excluyentes'.format(
            tp.lower(), pe.lower(), de.lower()
        )


if __name__ == '__main__':
    app.run_server(debug=True)
