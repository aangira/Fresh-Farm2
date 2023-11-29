from django.urls import path
from . import views

app_name='kisumu'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.details, name='detail'),
    path('feature/', views.features, name='features'),
    path('product/', views.product, name='product'),
    path('service/', views.services, name='services'),
    path('teams/', views.team, name='team'),
    path('testmonials/', views.testimonials, name='testimonials'),


]


