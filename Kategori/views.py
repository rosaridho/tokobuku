from django.shortcuts import render, redirect, get_list_or_404
from .models import agama,nonfiksi,romance,sastra,teknik
<<<<<<< HEAD
import subprocess
=======
>>>>>>> release

# Create your views here.
def kategori(request):
    agama_obj = agama.objects.all()
    nonfiksi_obj = nonfiksi.objects.all()
    romance_obj = romance.objects.all()
    sastra_obj = sastra.objects.all()
    teknik_obj = teknik.objects.all()
<<<<<<< HEAD

    if request.POST:
        # give the absolute path to your `text4midiAllMilisecs.py`
        # and for `tiger.mid`
        # subprocess.call(['python', '/path/to/text4midiALLMilisecs.py', '/path/to/tiger.mid'])

        subprocess.call('/home/alphatech/Desktop/Exercise_ATA/workdir/tokobuku/runsplit.sh')
        
    return render(request, 'kategori.html', {'agama_obj':agama_obj, 'nonfiksi_obj':nonfiksi_obj, 'romance_obj':romance_obj, 'sastra_obj':sastra_obj, 'teknik_obj':teknik_obj})
=======
    return render(request, 'kategori.html', {'agama_obj':agama_obj, 'nonfiksi_obj':nonfiksi_obj, 'romance_obj':romance_obj, 'sastra_obj':sastra_obj, 'teknik_obj':teknik_obj})
    
>>>>>>> release
