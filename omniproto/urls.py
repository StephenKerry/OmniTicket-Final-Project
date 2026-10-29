from django.contrib import admin
from django.urls import path
from queuedemo.views import home, api_message

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
     path("api/messages/", api_message)
]