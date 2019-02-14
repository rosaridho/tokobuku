from django.contrib import admin
from .models import Kategori

# Register your models here.
my_model = [Kategori]
admin.site.register(my_model)