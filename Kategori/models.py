from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Kategori(models.Model):
    judul = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 25)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    waktuTersedia = models.DateField(default = timezone.now)
    gambar = models.ImageField(upload_to='home')
    penulis = models.CharField(max_length = 50)

    def __str__(self):
        return self.judul