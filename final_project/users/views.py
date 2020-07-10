# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"


class ProfilePageView(TemplateView):
    template_name = "profile.html"
