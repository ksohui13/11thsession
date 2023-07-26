from django.shortcuts import render, redirect
from .models import Blog
from rest_framework import viewsets, permissions
from .sefializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer