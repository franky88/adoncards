from django.contrib import admin
from .models import CardAdd, BackgroundImage, CardCategory
# Register your models here.
admin.site.site_header = "AD ON GROUP"


@admin.register(CardAdd)
class CardAddAdmin(admin.ModelAdmin):
    list_display = ("__str__", "image_url")


admin.site.register(BackgroundImage)
admin.site.register(CardCategory)
