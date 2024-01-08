from django.shortcuts import render

from common.views import TitleMixin
from django.contrib.auth.views import TemplateView

class HomeView(TitleMixin, TemplateView):
    title = 'Блог'
    template_name = 'posts/index.html'
