# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Transaction
from trees.models import Tree


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfilePageView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "profile.html"
    login_url = "login"
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("dashboard")


class DashboardPageView(TemplateView, LoginRequiredMixin):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        trees_for_sale = Tree.objects.filter(owner_id=self.request.user.id)
        user_transactions = Transaction.objects.filter(user_id=self.request.user.id)

        transactions = list()
        for item in user_transactions:
            tree = Tree.objects.get(id=item.tree_id)

            if tree.sold == True:
                t_sale = "Sold"
            else:
                t_sale = "Bought"

            transactions.append(
                dict(
                    tree_name=tree.name,
                    date=item.date_time,
                    price=tree.price,
                    sale=t_sale,
                )
            )

        context["trees_for_sale"] = trees_for_sale
        context["transactions"] = transactions

        return context
