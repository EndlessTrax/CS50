# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy


from .models import Tree
from .forms import TreeCreationForm


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class MarketplacePageView(ListView):
    template_name = 'marketplace.html'
    model = Tree


class AddTreePageView(CreateView, LoginRequiredMixin):
    form_class = TreeCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "new_tree.html"


class SingleTreePageView(DetailView):
    template_name = "single_tree.html"
    model = Tree


class EditTreePageView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = 'edit_tree.html'
    login_url = "login"
    model = Tree
    fields = ("name", "species", "description", "location", "price", "picture")

    def get_success_url(self):
        return reverse_lazy('dashboard')
