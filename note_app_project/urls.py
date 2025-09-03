from django.contrib import admin
from django.urls import path, include
from notes.views import note_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('notes.urls')),  # signup
    path('', note_list, name='note_list'),
]
