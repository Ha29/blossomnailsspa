from django.contrib import admin

# Register your models here.
from .models import Person, PrivateSuggestion
admin.site.register(Person)
admin.site.register(PrivateSuggestion)
