from django.urls import path

from .views import HomePageView, MarketplacePageView, AddTreePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('market/', MarketplacePageView.as_view(), name='marketplace'),
    path('tree/new', AddTreePageView.as_view(), name='newtree'),
]