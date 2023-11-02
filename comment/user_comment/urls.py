from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('u_comment', views.u_comment, name="u_comment"),
]