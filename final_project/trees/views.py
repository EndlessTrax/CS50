# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect


from .models import Tree
from .forms import TreeCreationForm
from .locations import LOCATION_CHOICES
from users.models import Transaction


class HomePageView(TemplateView):
    template_name = "homepage.html"


class MarketplacePageView(ListView):
    template_name = "marketplace.html"
    model = Tree


class AddTreePageView(CreateView, LoginRequiredMixin):
    form_class = TreeCreationForm
    success_url = reverse_lazy("dashboard")
    template_name = "new_tree.html"


class SingleTreePageView(DetailView):
    template_name = "single_tree.html"
    model = Tree

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state_code = self.object.location

        for state in LOCATION_CHOICES:
            if state[0] == state_code:
                context["state"] = state[1]

        return context


class EditTreePageView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "edit_tree.html"
    login_url = "login"
    model = Tree
    fields = ("name", "species", "description", "location", "price", "picture")

    def get_success_url(self):
        return reverse_lazy("dashboard")


class DeleteTreePageView(DeleteView):
    template_name = "delete_tree.html"
    model = Tree
    success_url = reverse_lazy("dashboard")


class BuyTreePageView(TemplateView):
    template_name = "buy_tree_confirm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tree = Tree.objects.get(id=self.kwargs['pk'])
        context['tree'] = tree
        return context

    def post(self, request, *args, **kwargs):
        new_transaction = Transaction(
            user_id = request.user.id,
            tree_id = self.kwargs['pk'],
            bought = True
        )
        new_transaction.save()

        tree = Tree.objects.get(id=self.kwargs['pk'])
        tree.sold = True
        tree.save()

        return HttpResponseRedirect(reverse_lazy("dashboard"))
