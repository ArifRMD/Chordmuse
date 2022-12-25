# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Kategori(models.Model):
    nama = models.CharField(max_length=40)
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"

# Create your models here.
class chord(models.Model):
    songname = models.CharField(max_length=50,null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)
    date = models.IntegerField(null=True)
    body = RichTextUploadingField(blank=True,null=True,
                                    config_name='special',
                                    external_plugin_resources=[(
                                        'youtube',
                                        '/static/ckeditor_plugins/youtube/youtube/',
                                        'plugin.js',
                                    )],
                                    )
    
    def __str__(self):
        return self.songname

    class Meta:
        ordering =['songname']
        verbose_name_plural = "Kategori"