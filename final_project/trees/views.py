# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy


from .models import Tree
from .forms import TreeCreationForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class MarketplacePageView(ListView):
    template_name = 'marketplace.html'
    model = Tree

class AddTreePageView(CreateView):
    form_class = TreeCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "new_tree.html"
