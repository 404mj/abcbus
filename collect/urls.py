from django.urls import path
from . import views

app_name = 'collect'
urlpatterns = [
    path('pf/add/', views.add_pf, name='pfadd'),
    path('pf/list/', views.list_pf, name='pflist'),
    path('pf/edit/<int:pfid>', views.edit_pf, name='pfedit'),
    path('pf/del/<int:pfid>', views.delete_pf, name='pfdelete'),
    path('pf/summary', views.summary_pf, name='pfsummary')
]
