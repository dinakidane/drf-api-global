from django.urls import path
from .views import SubscriberListCreateView, SubscriberDetailView

urlpatterns = [
    path('subscribers/', SubscriberListCreateView.as_view(), name='subscriber-list-create'),
    path('subscribers/<int:subscribed_to_id>/', SubscriberDetailView.as_view(), name='subscriber-detail'),
]