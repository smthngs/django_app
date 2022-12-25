from django.urls import path
from .views import yazi_view

app_name = "yazi"

urlpatterns = [
    path('<str:slug>', yazi_view)
]

