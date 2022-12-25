from django.urls import path ,include
from Chord.views import *

urlpatterns = [
    path('',Admin, name='Admin'),
    path('Form', Form, name='Form'),
    path('Table', Table, name='Table'),
    path('Table_user',Table_user,name='Table_user'),
    path('Table/lihat/<str:id>', lihat_chord, name='lihat_chord'),
    path('Table/edit/<str:id>', edit_chord, name='edit_chord'),
    path('Table/delete/<str:id>', delete_chord, name='delete_chord'),
    path('ckeditors/', include('ckeditor_uploader.urls')),
]