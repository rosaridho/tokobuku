from django.contrib import admin
from .models import agama,nonfiksi,romance,sastra,teknik

# Register your models here.
my_model = [agama,nonfiksi,romance,sastra,teknik]
admin.site.register(my_model)