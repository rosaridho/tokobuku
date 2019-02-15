from django.urls import path, include
from . import views
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> release
from django.conf.urls import url

urlpatterns = [
    path('', views.kategori, name='kategori'),
    url(r'^run-sh/$', views.kategori, name='run_sh'),
<<<<<<< HEAD
]
=======
=======

urlpatterns = [
    path('', views.kategori, name='kategori'),
>>>>>>> release
]
>>>>>>> release
