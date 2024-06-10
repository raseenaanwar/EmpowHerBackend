# mentors/urls.py

from django.urls import path
from .views import MenteeBlockView, MenteeListView

urlpatterns = [
    path('mentee-list/', MenteeListView.as_view(), name='mentee-list'),
    path('<int:pk>/block/', MenteeBlockView.as_view(), name='mentee-block'),
    # Add other URLs as needed
]
