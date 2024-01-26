
from django.urls import path
from .views import LawyerDetailView, BlogCreateView, BlogListView

urlpatterns = [
    path('lawyers/<int:pk>/', LawyerDetailView.as_view(), name='lawyer-detail'),
    path('blogs/create/', BlogCreateView.as_view(), name='create-blog'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
]
