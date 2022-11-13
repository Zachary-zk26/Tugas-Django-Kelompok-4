from django.contrib import admin

from . models import Mahasiswa


class TampilGuest(admin.ModelAdmin):
    list_display=('nim','nama')
    list_display_links=(None)
    search_fields=('nim','nama')
admin.site.register(Mahasiswa,TampilGuest)