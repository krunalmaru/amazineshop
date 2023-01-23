from django.urls import path
from ecomapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contactus, name='contact'),
    path('about/', views.aboutus, name='aboutus'),
]
