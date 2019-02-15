from django.contrib import admin
from .models import buku

# Register your models here.
my_model = [buku]
admin.site.register(my_model)