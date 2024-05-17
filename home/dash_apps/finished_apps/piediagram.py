import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('PieDiagram', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode'),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])



def display_value(value):
    labels = ['Positivo', 'Negativo', 'Neutro']

    #Traer si es positivo, negativo y neutro
    y = ['Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Positivo', 'Neutro', 'Negativo', 'Positivo', 'Neutro', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Neutro', 'Positivo', 'Negativo', 'Positivo', 'Neutro', 'Negativo', 'Positivo', 'Neutro', 'Positivo']
    
    values = [(y.count('Positivo')/len(y)) * 100, (y.count('Negativo')/len(y)) * 100, (y.count('Neutro')/len(y)) * 100 ]

    graph = go.Pie(
        labels=labels,
        values=values,
        hole = 0.3
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(title='Calificación comentario'),

    )
    return {'data': [graph], 'layout': layout}