from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView


urlpatterns = [
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='edit_blog'),
    path('new/', BlogCreateView.as_view(), name='new'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogListView.as_view(), name='home')
]