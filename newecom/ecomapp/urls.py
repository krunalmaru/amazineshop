from django.urls import path
from ecomapp import views
urlpatterns = [
    path('', views.home, name='home')
]
