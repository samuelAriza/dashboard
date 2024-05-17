import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data = {
    'Hour': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
    'Positive': [10, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    'Negative': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
    'Neutral': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
}

df = pd.DataFrame(data)

app = DjangoDash('HoursDiagram', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode'),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])



def display_value(value):
    # Tu lógica para actualizar el gráfico aquí
    # Puedes usar hoverData para obtener la hora seleccionada

    # Ejemplo de gráfico de barras apiladas
    trace1 = go.Bar(
        x=df['Hour'],
        y=df['Positive'],
        name='Positive',
        marker=dict(color='green')
    )
    trace2 = go.Bar(
        x=df['Hour'],
        y=df['Negative'],
        name='Negative',
        marker=dict(color='red')
    )
    trace3 = go.Bar(
        x=df['Hour'],
        y=df['Neutral'],
        name='Neutral',
        marker=dict(color='grey')
    )

    data = [trace1, trace2, trace3]
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        barmode='stack',
        title='Hourly Comments Analysis',
        xaxis=dict(title='Hour of the Day'),
        yaxis=dict(title='Number of Comments')
    )

    return {'data': data, 'layout': layout}