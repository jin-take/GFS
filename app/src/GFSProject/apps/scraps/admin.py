from django.contrib import admin
from .models import Tag, Event, Category

# Register your models here.


admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Category)