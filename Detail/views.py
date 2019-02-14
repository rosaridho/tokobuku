from django.shortcuts import render

# Create your views here.
def detailbook(request):
    return render(request, 'detailbuku.html', {'buku_obj':buku_obj})