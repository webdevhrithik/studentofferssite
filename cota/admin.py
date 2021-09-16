from django.contrib import admin
from .models import *

admin.site.site_header = 'Student Cota Management Dashboard'

admin.site.register(Category)
admin.site.register(Offer)