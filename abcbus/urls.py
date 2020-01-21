from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='collect/index.html'), name='home'),
    path('collect/', include('collect.urls')),
    path('collect/', include('django.contrib.auth.urls')),
]
