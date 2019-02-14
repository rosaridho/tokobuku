from django.urls import path, include
from . import views
<<<<<<< HEAD
from django.conf.urls import url

urlpatterns = [
    path('', views.kategori, name='kategori'),
    url(r'^run-sh/$', views.kategori, name='run_sh'),
=======

urlpatterns = [
    path('', views.kategori, name='kategori'),
>>>>>>> release
]