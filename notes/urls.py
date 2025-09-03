from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.note_list, name="note_list"),
    path("new/", views.note_create, name="note_create"),
    path("<int:pk>/edit/", views.note_edit, name="note_edit"),
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),

    # API for Streamlit
    path("api/notes/", views.notes_api, name="notes_api"),
]
