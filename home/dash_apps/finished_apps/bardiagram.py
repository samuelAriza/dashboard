import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('BarDiagram', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode'),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])



def display_value(value):
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #y = calificaciones de todos los comentarios
    y = [1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 9, 10, 10, 10]
    y1 = [y.count(1), y.count(2), y.count(3), y.count(4), y.count(5), y.count(6), y.count(7), y.count(8), y.count(9), y.count(10)]


    graph = go.Bar(
        x=x1,
        y=y1,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title='Hourly Comments Analysis',
        xaxis=dict(title='Calificación comentario'),
        yaxis=dict(title='Cantidad de comentarios'),

    )
    return {'data': [graph], 'layout': layout}