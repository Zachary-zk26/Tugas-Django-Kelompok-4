from django.contrib import admin

from . models import Post,Kelas

class TampilKelas(admin.ModelAdmin):
    list_display=('mata_kuliah','dosen','kelas')
    list_display_links=(None)
    search_fields=('mata_kuliah','dosen')
admin.site.register(Post,TampilKelas)
admin.site.register(Kelas)
