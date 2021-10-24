from django.contrib import admin
from .models import CardAdd, BackgroundImage, CardCategory
# Register your models here.
admin.site.site_header = "AD ON GROUP"
admin.site.register(CardAdd)
admin.site.register(BackgroundImage)
admin.site.register(CardCategory)
