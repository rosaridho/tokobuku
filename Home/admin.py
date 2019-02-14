from django.contrib import admin
from .models import Buku

# Register your models here.
my_model = [Buku]
admin.site.register(my_model)