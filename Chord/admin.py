from django.contrib import admin
from Chord.models import *
# Register your models here.
admin.site.register(Kategori)



class ChordAdmin(admin.ModelAdmin):
    list_display = ['songname','date','kategori','body']
admin.site.register(chord, ChordAdmin)

#