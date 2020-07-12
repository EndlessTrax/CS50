from django.urls import path

from .views import (
    HomePageView,
    MarketplacePageView,
    AddTreePageView,
    SingleTreePageView,
    EditTreePageView,
    DeleteTreePageView,
    BuyTreePageView
)


urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("market/", MarketplacePageView.as_view(), name="marketplace"),
    path("tree/new/", AddTreePageView.as_view(), name="newtree"),
    path("tree/<int:pk>/", SingleTreePageView.as_view(), name="single_tree"),
    path("tree/edit/<int:pk>/", EditTreePageView.as_view(), name="edit_tree"),
    path("tree/delete/<int:pk>/", DeleteTreePageView.as_view(), name="delete_tree"),
    path("tree/buy/<int:pk>/", BuyTreePageView.as_view(), name="buy_tree"),
]
