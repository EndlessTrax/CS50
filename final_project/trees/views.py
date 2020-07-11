# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


# from .models import Tree
from .forms import TreeCreationForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class MarketplacePageView(TemplateView):
    template_name = 'marketplace.html'


class AddTreePageView(CreateView):
    form_class = TreeCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "tree.html"
