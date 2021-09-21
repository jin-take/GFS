from django.urls import path
from . import views

app_name = 'scraps'

urlpatterns = [
    path('list', views.ScrapsList.as_view(), name='scraps_list'),
    path('detail', views.ScrapsDetail.as_view(), name='scraps_detail'),
    path('edit', views.ScrapsEdit.as_view(), name='scraps_edit'),
    path('post', views.ScrapsPost.as_view(), name='scraps_post'),
]
