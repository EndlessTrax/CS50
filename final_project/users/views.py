# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DashboardPageView(TemplateView, LoginRequiredMixin):
    template_name = "dashboard.html"


class ProfilePageView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "profile.html"
    login_url = "login"
    model = CustomUser
    fields = ('display_name', 'avatar')

    def get_success_url(self):
        return reverse_lazy('dashboard')
