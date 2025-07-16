"""
URL configuration for gemini_test_generator project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_generator.urls')),  # This line includes your app's URLs at the root
] 