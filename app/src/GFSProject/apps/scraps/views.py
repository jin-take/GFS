from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class ScrapsList(TemplateView):
    template_name = 'scraps/list.html'


class ScrapsDetail(TemplateView):
    template_name = 'scraps/detail.html'


class ScrapsEdit(TemplateView):
    template_name = 'scraps/edit.html'


class ScrapsPost(TemplateView):
    template_name = 'scraps/post.html'
