from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

def comments(request):
    comments = ["Samuel", "Andres", "Ariza", "Gomez"]

    return render(request, 'home/comments.html', {'comments':comments})

def analysis(request):
    comments = ["Samuel", "Andres", "Ariza", "Gomez", "Beto"]
    return render(request, "home/analysis.html", {'comments':comments})

def charts(request):
    return render(request, "home/charts.html")
