from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.add_show),
    path('submit_show', views.submit_show),
    path('shows/<int:id>', views.display_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.submit_edit),
    path('shows/<int:id>/delete', views.delete_show),
]