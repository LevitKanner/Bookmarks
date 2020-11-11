from django.contrib import admin
from .models import Image

# Register your models here.
@admin.register(Image)
class ImageAdminManager(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'created')
    list_filter = ('created',)