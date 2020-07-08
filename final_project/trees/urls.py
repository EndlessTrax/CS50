from django.urls import path

from .views import HomePageView, MarketplacePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('market/', MarketplacePageView.as_view(), name='marketplace'),
]