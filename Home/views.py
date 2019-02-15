from django.shortcuts import render, redirect, get_list_or_404
from .forms import PostForm
from .models import buku

# Create your views here.
def halamanHome(request):
    buku_obj = buku.objects.all()
    return render(request, 'home.html', {'buku_obj':buku_obj})

def lengkapBuku(request, post_id):
    post_num = get_list_or_404(buku, id=post_id)
    return render(request, 'detailbuku.html', {'buku_obj':post_num})

def input_buku(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('input_buku')
    else:
        form = PostForm()

    return render(request, 'tambahbuku.html', {'form':form})

def download(request):
    return render(request, 'download.html')