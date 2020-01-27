from django.urls import path
from . import views

app_name = 'collect'
urlpatterns = [
    path('pf/add/', views.add_pf, name='pfadd'),
    path('pf/list/', views.list_pf, name='pflist')
]
