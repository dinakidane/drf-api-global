from django.urls import path
from .views import FavouriteListCreateView, FavouriteDetailView

urlpatterns = [
    path('favourites/', FavouriteListCreateView.as_view(), name='favourite-list'),
    path('favourites/<int:post_id>/', FavouriteDetailView.as_view(), name='favourite-detail'),  # For unliking a post
]