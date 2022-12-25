from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path ,include

from . views import *
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('about', about, name='about'),
    path('dashboard/',include('Chord.urls')),
    path('home/lihat/<str:id>', Detail_chord, name='Detail_chord'),
    path('Login/',Login,name='Login'),
    path('create/',create,name='create'),
    path('logout/',logout_admin,name='logout'),
    path('POP',POP, name='POP'),
    path('ROCK',ROCK, name='ROCK'),
    path('JAZZ',JAZZ, name='JAZZ'),
    path('REAGGEA',REAGGEA, name='REAGGEA'),
    path('PUNK',PUNK, name='PUNK'),
    path('ckeditors/', include('ckeditor_uploader.urls'))

   ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)