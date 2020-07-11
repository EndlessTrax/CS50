from django.urls import path, include

from .views import DashboardPageView, ProfilePageView, SignUpView


urlpatterns = [
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]