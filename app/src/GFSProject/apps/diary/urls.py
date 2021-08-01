from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('list', views.DiaryList.as_view(), name='diary_list'),
    path('detail', views.DiaryDetail.as_view(), name='diary_detail'),
    path('edit', views.DiaryEdit.as_view(), name='diary_edit'),
    path('post', views.DiaryPost.as_view(), name='diary_post'),
]
