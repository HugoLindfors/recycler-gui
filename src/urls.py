from django.contrib import admin
from django.urls import path
from .views import recycler

urlpatterns = [
    path("", recycler, name="src"),
    path("admin/", admin.site.urls),
]
