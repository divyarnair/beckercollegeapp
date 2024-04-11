from django.contrib import admin

# Register your models here.
from .models import Register,Customer


admin.site.register(Register)
admin.site.register(Customer)
