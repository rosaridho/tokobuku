from django.shortcuts import render, redirect, get_list_or_404
from .models import agama,nonfiksi,romance,sastra,teknik
import subprocess


# Create your views here.
def kategori(request):
    agama_obj = agama.objects.all()
    nonfiksi_obj = nonfiksi.objects.all()
    romance_obj = romance.objects.all()
    sastra_obj = sastra.objects.all()
    teknik_obj = teknik.objects.all()

    if request.POST:
        subprocess.call('/home/alphatech/Desktop/Exercise_ATA/workdir/tokobuku/runsplit.sh')
                         
    return render(request, 'kategori.html', {'agama_obj':agama_obj, 'nonfiksi_obj':nonfiksi_obj, 'romance_obj':romance_obj, 'sastra_obj':sastra_obj, 'teknik_obj':teknik_obj})

