from django.contrib import admin
from .models import Publisher, Book, GreatQuote

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(GreatQuote)