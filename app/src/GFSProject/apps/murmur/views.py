from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MurmurList(TemplateView):
    template_name = 'murmur/list.html'


class MurmurDetail(TemplateView):
    template_name = 'murmur/detail.html'


class MurmurEdit(TemplateView):
    template_name = 'murmur/edit.html'


class MurmurPost(TemplateView):
    template_name = 'murmur/post.html'
