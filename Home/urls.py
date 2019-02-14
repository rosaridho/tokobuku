from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanHome, name='home'),
    path('',views.detailbook, name='detail')
    # path('<int:post_id>', views.idpost_blog, name='idpost_blog'),
]