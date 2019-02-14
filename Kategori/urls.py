from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.kategori, name='kategori'),
    url(r'^run-sh/$', views.kategori, name='run_sh'),
]