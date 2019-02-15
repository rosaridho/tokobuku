from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import datetime
from django.utils import timezone

# Create your models here.
class agama(models.Model):
    gambar = models.ImageField(upload_to='kategori')
    judul = models.CharField(max_length = 50)
    penulis = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    ketersediaan = models.CharField(max_length = 50)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 50)
  
    def __str__(self):
        return self.judul

class nonfiksi(models.Model):
    gambar = models.ImageField(upload_to='kategori')
    judul = models.CharField(max_length = 50)
    penulis = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    ketersediaan = models.CharField(max_length = 50)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 50)
  
    def __str__(self):
        return self.judul

class romance(models.Model):
    gambar = models.ImageField(upload_to='kategori')
    judul = models.CharField(max_length = 50)
    penulis = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    ketersediaan = models.CharField(max_length = 50)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 50)
  
    def __str__(self):
        return self.judul


class sastra(models.Model):
    gambar = models.ImageField(upload_to='kategori')
    judul = models.CharField(max_length = 50)
    penulis = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    ketersediaan = models.CharField(max_length = 50)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 50)
  
    def __str__(self):
        return self.judul

class teknik(models.Model):
    gambar = models.ImageField(upload_to='kategori')
    judul = models.CharField(max_length = 50)
    penulis = models.CharField(max_length = 50)
    publisher = models.CharField(max_length = 50)
    ketersediaan = models.CharField(max_length = 50)
    harga = models.CharField(max_length = 50)
    hargadiskon = models.CharField(max_length = 50)
    kategori = models.CharField(max_length = 50)
  
    def __str__(self):
        return self.judul