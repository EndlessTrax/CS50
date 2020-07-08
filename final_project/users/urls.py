from django.urls import path

from .views import DashboardPageView, ProfilePageView


urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
]