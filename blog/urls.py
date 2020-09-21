from django.urls import path
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, PostCreateClean
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<pk>/cleaned/', PostCreateClean.as_view(), name='post-clean'),
]
