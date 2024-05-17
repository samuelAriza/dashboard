from django.urls import path
from . import views
from home.dash_apps.finished_apps import histogramdiagram, bardiagram, piediagram, hours, table1


urlpatterns =[
    path('', views.comments, name='comments'),
    path('analysis/', views.analysis, name='analysis'),
    path('charts/', views.charts, name='charts'),
]