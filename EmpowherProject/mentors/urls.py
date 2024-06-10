# mentors/urls.py

from django.urls import path
from .views import MentorBlockView, MentorListView
from . import views

urlpatterns = [
    path('mentor-list/', MentorListView.as_view(), name='mentor-list'),
    path('<int:pk>/block/', MentorBlockView.as_view(), name='mentor-block'),
    path('create_general_user_profile/', views.create_general_user_profile, name='create_general_user_profile'),
    # Add other URLs as needed
]

