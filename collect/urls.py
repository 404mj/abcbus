from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'collect'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='collect/home.html'), name='home'),
    # path('login', views.login, 'login'),
]
