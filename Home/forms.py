from django import forms
from .models import buku

class PostForm(forms.ModelForm):

    class Meta:
        model = buku
        fields = ('gambar', 'judul', 'penulis','publisher', 'ketersediaan', 'harga','hargadiskon', 'kategori', 'sinopsis')