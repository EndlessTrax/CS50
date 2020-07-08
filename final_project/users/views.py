# from django.shortcuts import render
from django.views.generic import TemplateView


class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'


class ProfilePageView(TemplateView):
    template_name = 'profile.html'