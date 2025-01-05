from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView


urlpatterns = [
    path('new/', BlogCreateView.as_view(), name='new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home')
]