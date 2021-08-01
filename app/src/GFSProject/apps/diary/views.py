from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class DiaryList(TemplateView):
    template_name = 'diary/list.html'


class DiaryDetail(TemplateView):
    template_name = 'diary/detail.html'


class DiaryEdit(TemplateView):
    template_name = 'diary/edit.html'


class DiaryPost(TemplateView):
    template_name = 'diary/post.html'
