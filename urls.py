# document_summarizer/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('summarizer.urls')),  # Include the URLs from your app
]
