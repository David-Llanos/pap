import sys

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


### TABLA GLOBAL
problemas = {
    'Personal': [u'Una relación amorosa', 'Depresión', 'Desempleo'],
    'Familiar': [u'Los hijos', 'Los suegros', 'Otros miembros de la familia'],
    'Laboral': [u'Desmotivación', 'Demasiada presión', 'Falta de oportunidades de crecimiento']
}

### ESTILO E INICIAR APP
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### FORMATO PARA DEFINIR LAS OPCIONES DEL USUARIO
app.layout = html.Div([
    html.H5("1. Seleccione tipo de problema"),
    dcc.RadioItems(id="tipo_problema", options=[{"label":x,"value":x} for x in problemas], value=""),

    html.Br(),
    html.H5(u"2. Problema específico", id= 'titulo_problema_especifico', style={'display':'none'}),
    dcc.RadioItems(id='problema_especifico', value="", style= {'display':'block'})

])

### ACTUALIZAR OPCIONES PARA CADA TIPO DE PROBLEMA
@app.callback(
    Output('problema_especifico', 'options'),
    Input('tipo_problema', 'value'))
def def_problema_seleccionado(problema_seleccionado):
    return [{'label': i, 'value': i} for i in problemas[problema_seleccionado]]

### OCULTAR/MOSTRAR PREGUNTA SOBRE PROBLEMA ESPECIFICO
@app.callback(
    Output('problema_especifico', 'labelStyle'),
    Output('titulo_problema_especifico', 'style'),
    [Input('tipo_problema', 'value')])
def def_mostrar_prob_especifico(mostrar_opciones):
    if mostrar_opciones != '':
        return [{'display': 'block'}, {'display': 'block'}]
    if mostrar_opciones == '':
        return [{'display': 'none'}, {'display': 'none'}]



if __name__ == '__main__':
    app.run_server(debug=True)