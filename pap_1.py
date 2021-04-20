import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.H5 import H5

import dash_bootstrap_components as dbc

from settings import config, about


import logging
import sys


external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])
#server=app.server

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

problemas = {
    'Personal': [u'Cambios', 'Proyecto de vida', 'Percecpión de sí mismo'],
    'Familiar': [u'Con su posición en la familia', 'En su núcleo familiar : padres e hijos', 'Con la Familia extensa: otros familiares'],
    'Laboral': [u'Con su jefe(a)', 'Con compañeros de trabajo', 'Con sus Condiciones laborales'],
    'Social': [u'Amigos', 'Vecinos', 'Relaciones interpersonales en general'],
    'Pareja': [u'Tipo de vínculo', 'Comunicación', 'Relaciones familiares', 'Relaciones amigos', 'Problemas económicos', 'Intimidad']
}

soluciones = {
    'Personal': [u'Cambios-solucion', 'Proyecto de vida-solucion', 'Percecpión de sí mismo-solucion'],
    'Familiar': [u'Con su posición en la familia-solucion', 'En su núcleo familiar-solucion : padres e hijos-solucion', 'Con la Familia extensa: otros familiares-solucion'],
    'Laboral': [u'Con su jefe(a)-solucion', 'Con compañeros de trabajo-solucion', 'Con sus Condiciones laborales-solucion'],
    'Social': [u'Amigos-solucion', 'Vecinos-solucion', 'Relaciones interpersonales en general-solucion'],
    'Pareja': [u'Tipo de vínculo-solucion', 'Comunicación-solucion', 'Relaciones familiares-solucion', 'Relaciones amigos-solucion', 'Problemas económicos-solucion', 'Intimidad-solucion']
}
# App Instance
app = dash.Dash(name=config.name, assets_folder=config.root+"/application/static", external_stylesheets=[dbc.themes.CERULEAN, config.fontawesome])
app.title = config.name




# Navbar
navbar = dbc.Nav(className="nav nav-pills", children=[
    ## logo/home
    #dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    ## about
            dbc.NavItem(html.Div([
                dbc.NavLink("About", href="/", id="about-popover", active=False),
                dbc.Popover(id="about", is_open=False, target="about-popover", children=[
                    dbc.PopoverHeader("How it works"), dbc.PopoverBody(about.txt)
                ])
            ]))
    ## links
    #dbc.DropdownMenu(label="Links", nav=True, children=[
    #    dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"), "  Contacts"], href=config.contacts, target="_blank"),
    #    dbc.DropdownMenuItem([html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank")
    #])
])

# Inputs
inputs = dbc.FormGroup([

    html.Br(),
    html.H5("1. Seleccione tipo de situación", id= 'titulo_tipo_problema', style={'display':'block'}),
    dcc.RadioItems(id="tipo_problema", options=[{"label":x,"value":x} for x in problemas], value="",
                   labelStyle={'display': 'block'}),

    html.Br(),
    html.H5(u"2. Situación específica", id= 'titulo_problema_especifico', style={'display':'none'}),
    dcc.RadioItems(id='problema_especifico', value="",
                   labelStyle={'display': 'none'}
                   ),

    html.Br(),
    html.H5(u"3. ¿Qué soluciones ha intentado?", id= 'titulo_soluciones_intentadas', style={'display':'none'}),
    dcc.RadioItems(id='soluciones_intentadas', value="",
                   labelStyle={'display': 'block'}
                   ),


    html.Br(),
    html.H5(u"4. ¿En esta situación debe tener tomar una decisión entre opciones mutuamente excluyentes?", id= 'titulo_decision_excluyente', style={'display':'none'}),
    dcc.RadioItems(id='decision_excluyente', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                   labelStyle={'display': 'block'}

                   ),

    html.Br(),
    html.H5(u"5. ¿Es esta una decisión que afecta sus principios y valores?", id= 'titulo_decision_afecta_valores', style={'display':'none'}),
    dcc.RadioItems(id='decision_afecta_valores', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),


    html.Br(),
    html.H5(u"6. Es difícil controlar las emociones en esta situación?", id= 'titulo_emociones_desbordadas', style={'display':'none'}),
    dcc.RadioItems(id='emociones_desbordadas', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'none'}
                   ),

    html.Br(),
    html.H5(u"7a. Diría usted que está confundido(a) respecto a cuáles son los objetivos por seguir?", id= 'titulo_identificar_objetivo', style={'display':'none'}),
    dcc.RadioItems(id='identificar_objetivo', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),

    html.Br(),
    html.H5(u"7b. Diría usted que no es fácil identificar la forma de alcanzar sus objetivos?", id= 'titulo_alcanzar_objetivo', style={'display':'none'}),
    dcc.RadioItems(id='alcanzar_objetivo', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),

    html.Br(),
    html.H5(u"7c. Alguno de los involucrados ha decidido cerrar la comunicación?", id= 'titulo_cerrar_comunicacion', style={'display':'none'}),
    dcc.RadioItems(id='cerrar_comunicacion', value="",
                    options=[
                                {'label': u'Sí', 'value': 'si'},
                                {'label': 'No', 'value': 'no'}
                            ] ,
                    labelStyle={'display': 'block'}
                   ),
    html.Br(),
    html.H5(u"7d. Considera usted que es muy difícil construir acuerdos con los involucrados?", id= 'titulo_construir_acuerdos', style={'display':'none'}),
    dcc.RadioItems(id='construir_acuerdos', value="",
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
        dbc.Col(md=5, children=[
            inputs,
            html.Br(),html.Br(),html.Br(),
            html.Div(id="output-panel")
        ]),
        ### plots
        dbc.Col(md=7, children=[
            dbc.Col(html.H4("Dilemas, Problemas o Conflictos"), width={"size":6,"offset":3}),

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
                                ),
                                    dcc.Textarea(
                                          id='diagnostico',
                                          value='',
                                          style={'display':'none'},
                                        ),

                    dbc.Tab(dcc.Graph(id="proyecto_final"), label="Proyecto final")
            ])
        ])
    ])
])

server=app.server
#####CALLBACKS


### ACTUALIZAR OPCIONES PARA CADA TIPO DE PROBLEMA
@app.callback(
    Output('problema_especifico', 'options'), #options property is updated here
    Input('tipo_problema', 'value'))
def def_problema_seleccionado(problema_seleccionado):
    return [{'label': i, 'value': i} for i in problemas[problema_seleccionado]]

### OCULTAR/MOSTRAR PREGUNTA SOBRE PROBLEMA ESPECIFICO
@app.callback(
    Output('problema_especifico', 'labelStyle'),
    Output('titulo_problema_especifico', 'style'),
    Output('problema_especifico', 'value'),
    Input('tipo_problema', 'value')
    )
def def_opciones_prob_especifico(tp):
    if tp != '' :
        return [{'display': 'block'}, {'display': 'block'},'']
    elif tp == '':
        return [{'display': 'none'}, {'display': 'none'},'']


### OCULTAR/MOSTRAR PREGUNTA SOBRE SOLUCIONES INTENTADAS



@app.callback(
    Output('soluciones_intentadas', 'options'),
    #Output('soluciones_intentadas', 'labelStyle'),
    Output('titulo_soluciones_intentadas', 'style'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value')
    )
def def_opciones_solu_intentadas(tp, pe):
    print(pe)
    if tp != '' and pe !='' :
        return [ [{'label': i, 'value': i} for i in soluciones[tp]], {'display': 'block'} ]
    else :
        return [[], {'display': 'none'}]


### OCULTAR/MOSTRAR PREGUNTA SOBRE DECISION EXCLUYENTE
@app.callback(
    Output('decision_excluyente', 'value'),
    Output('decision_excluyente', 'labelStyle'),
    Output('titulo_decision_excluyente', 'style'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('soluciones_intentadas', 'value')
    )
def def_mostrar_decision_excluyente(tp, pe, si): #tp: tipo de problema; de : decision excluyente
    if tp != '' and pe != '' and si != '':
        return ['',{'display': 'block'}, {'display': 'block'}]
    else:
        return ['',{'display': 'none'}, {'display': 'none'}]

### OCULTAR/MOSTRAR PREGUNTA SOBRE DECISION AFECTA VALORES
@app.callback(
    Output('decision_afecta_valores', 'value'),
    Output('decision_afecta_valores', 'labelStyle'),
    Output('titulo_decision_afecta_valores', 'style'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('soluciones_intentadas', 'value'),
    Input('decision_excluyente', 'value')
    )
def def_mostrar_decision_excluyente(tp, pe, si, de): #tp: tipo de problema; de : decision excluyente
    if tp != '' and pe != '' and si != '' and de != '':
        return ['',{'display': 'block'}, {'display': 'block'}]
    else:
        return ['',{'display': 'none'}, {'display': 'none'}]

### OCULTAR/MOSTRAR PREGUNTA SOBRE EMOCIONES DESBORDADAS
@app.callback(
    Output('emociones_desbordadas', 'labelStyle'),
    Output('titulo_emociones_desbordadas', 'style'),
    Input('decision_excluyente', 'value'),
    Input('decision_afecta_valores', 'value')
    )
def def_emociones_desbordadas(de, av):
    if de == 'no' and av!='' :
        return [{'display': 'block'}, {'display': 'block'}]
    else :
        return [{'display': 'none'}, {'display': 'none'}]


### OCULTAR/MOSTRAR PREGUNTA SOBRE IDENTIFICAR OBJETIVO
@app.callback(
    Output('identificar_objetivo', 'labelStyle'),
    Output('titulo_identificar_objetivo', 'style'),
    Input('emociones_desbordadas', 'value')
    )
def def_identificar_objetivo(ed):
    if ed !='' :
        return [{'display': 'block'}, {'display': 'block'}]
    else :
        return [{'display': 'none'}, {'display': 'none'}]


### OCULTAR/MOSTRAR PREGUNTA SOBRE ALCANZAR OBJETIVO
@app.callback(
    Output('alcanzar_objetivo', 'labelStyle'),
    Output('titulo_alcanzar_objetivo', 'style'),
    Input('identificar_objetivo', 'value')
    )
def def_alcanzar_objetivo(io):
    if io =='no' :
        return [{'display': 'block'}, {'display': 'block'}]
    else :
        return [{'display': 'none'}, {'display': 'none'}]


### OCULTAR/MOSTRAR PREGUNTA SOBRE CERRAR COMUNICACION (SOLO PARA CONFLICTO = EMOCION DESBORDADA : SI)
@app.callback(
    Output('cerrar_comunicacion', 'labelStyle'),
    Output('titulo_cerrar_comunicacion', 'style'),
    Input('emociones_desbordadas', 'value'),
    Input('alcanzar_objetivo', 'value')
    )
def def_cerrar_comunicaciono(ed, ao):
    if ed=='si' and ao !='' :
        return [{'display': 'block'}, {'display': 'block'}]
    else :
        return [{'display': 'none'}, {'display': 'none'}]

### OCULTAR/MOSTRAR PREGUNTA SOBRE CONSTRUIR ACUERDOS (SOLO PARA PROBLEMA = EMOCION DESBORDADA : NO)
@app.callback(
    Output('construir_acuerdos', 'labelStyle'),
    Output('titulo_construir_acuerdos', 'style'),
    Input('emociones_desbordadas', 'value'),
    Input('alcanzar_objetivo', 'value')
    )
def def_construir_acuerdos(ed, ao):
    if ed=='no' and ao !='' :
        return [{'display': 'block'}, {'display': 'block'}]
    else :
        return [{'display': 'none'}, {'display': 'none'}]

### DECIDIR PREGUNTA: VALORES U OBJETIVO DEPENDIENDO DE DECISION EXCLUYENTE
'''
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
'''



### DIAGNOSTICO
@app.callback(
    Output('diagnostico', 'style'),
    Output('diagnostico', 'value'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('decision_excluyente', 'value'),
    Input('decision_afecta_valores', 'value'),
    Input('emociones_desbordadas', 'value'),
    Input('identificar_objetivo', 'value'),
    Input('alcanzar_objetivo', 'value')
    )
def def_diagnostico(tp, pe, de, av, ed,io, ao):
    #print ( tp, pe, de, av,ed,io, ao)
    if tp != '' and pe != ''and de == 'si' and av != '':
        return {'display': 'block','width': '100%', 'height': 100, 'font-size': '2rem', 'margin-top': '40px' }, u'Usted está enfrentando un Dilema'
    elif tp != '' and pe != '' and de == 'no' and ed== 'si' and io != '':
        return {'display': 'block','width': '100%', 'height': 100, 'font-size': '2rem' , 'margin-top': '40px'}, u'Usted está enfrentando un Conflicto'
    elif tp != '' and pe != '' and de == 'no' and ed== 'no' and io != '':
        return {'display': 'block','width': '100%', 'height': 100, 'font-size': '2rem' , 'margin-top': '40px'}, u'Usted está enfrentando un Problema'
    elif tp != '' and pe != ''or de != '' :
        return {'display': 'none','width': '100%', 'height': 100, 'font-size': '2rem' , 'margin-top': '40px'}, u''

### DESCRIPCION DEL PROBLEMA
@app.callback(
    Output('descripcion_problema', 'children'),
    Input('tipo_problema', 'value'),
    Input('problema_especifico', 'value'),
    Input('decision_excluyente', 'value'),
    Input('decision_afecta_valores', 'value'),
    Input('emociones_desbordadas', 'value'),
    Input('identificar_objetivo', 'value'),
    Input('alcanzar_objetivo', 'value')
    )
def def_descripcion_problema(tp, pe, de, av, ed ,io, ao):
    if tp != '' and pe != ''and de == 'si' and av != '':
            return u'Usted ha señalado que tiene una situación {}\
                relacionada   {}.\
                Esta situación  {} lo(a) obliga a tomar decisiones excluyentes y \
                {} afecta sus valores.'.format(tp.lower(), pe.lower(), de.lower(), av.lower())

    elif tp != '' and pe != '' and de == 'no' and av != '' and ed== 'si'  and io != '':
            return  u'Usted ha señalado que tiene una situación {}\
                    relacionada   {}.\
                    Esta situación  {} lo(a) obliga a tomar decisiones excluyentes y \
                    {} afecta sus valores.\
                    La situación {} ha implicado desbordamiento de emociones y {} hace que sea difícil identificar sus objetivos.'\
                    .format(tp.lower(), pe.lower(), de.lower(), av.lower(), ed.lower(),io.lower())

    elif tp != '' and pe != '' and de == 'no' and av != '' and ed== 'no'  and io != '':
            return u'Usted ha señalado que tiene una situación {}\
                    relacionada   {}.\
                    Esta situación  {} lo(a) obliga a tomar decisiones excluyentes y {} ha hecho que sea difícil identificar sus objetivos.\
                    La situación {} ha implicado desbordamiento de emociones'\
                    .format(tp.lower(), pe.lower(), de.lower(), av.lower(), ed.lower(),io.lower())

    elif tp != '' and pe != ''or de == 'no' or av== 'no':
        return ''

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=True)
