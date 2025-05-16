from django.contrib import admin
from .models import Order, RegistrationLinks
from django.utils.safestring import mark_safe

admin.site.register(Order)
admin.site.register(RegistrationLinks)

