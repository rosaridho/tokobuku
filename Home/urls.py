from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanHome, name='home'),
    path('<int:post_id>', views.lengkapBuku, name='lengkapBuku'),
    path('tambahbuku', views.input_buku, name='input_buku'),
]