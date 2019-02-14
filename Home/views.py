from django.shortcuts import render, redirect, get_list_or_404
from .models import buku

# Create your views here.
def halamanHome(request):
    buku_obj = buku.objects.all()
    return render(request, 'home.html', {'buku_obj':buku_obj})