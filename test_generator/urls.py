from django.urls import path
from . import views

app_name = 'test_generator'
 
urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_test, name='generate_test'),
] 