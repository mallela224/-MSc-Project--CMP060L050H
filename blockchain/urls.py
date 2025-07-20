from django.urls import path
from .views import BlockListView

urlpatterns = [
    path('', BlockListView.as_view(), name='blockchain-list'),
] 