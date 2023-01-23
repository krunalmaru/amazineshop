from django.urls import path
from auth import views

urlpatterns = [
    path('signup/', views.signup, name='loginview'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='loginview'),

]
