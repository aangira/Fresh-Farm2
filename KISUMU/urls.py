from django.urls import path
from . import views

app_name='kisumu'

urlpatterns = [
    path('', views.home, name='home'),
    path('viewdata', views.team, name="team")


]


