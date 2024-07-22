from django.contrib import admin
from .models import Keyword,SearchResult

# Register your models here.

admin.site.register(Keyword)
admin.site.register(SearchResult)