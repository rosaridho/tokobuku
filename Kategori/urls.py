from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanKategori, name='kategori'),
    # path('<int:post_id>', views.idpost_blog, name='idpost_blog'),
]