from django.urls import path
from authuse import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),

]
