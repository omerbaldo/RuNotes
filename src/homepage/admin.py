from django.contrib import admin

# Register your models here.
from .models import post
from .models import terms


admin.site.register(post)
admin.site.register(terms)
