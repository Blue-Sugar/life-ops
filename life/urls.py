from django.urls import path

from . import views


app_name = 'life'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]