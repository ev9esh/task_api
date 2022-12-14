from django.urls import include, path
from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]
