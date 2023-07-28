from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin


router = DefaultRouter()
router.register('', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
