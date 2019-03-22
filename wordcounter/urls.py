from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('wordcounter/', views.index, name="wordcounter"),
    path('count/', views.count, name="count"),
]
