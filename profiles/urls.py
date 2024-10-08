from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.UserProfileListView.as_view()),
    path('profiles/<int:pk>/', views.UserProfileDetailView.as_view()),
]
