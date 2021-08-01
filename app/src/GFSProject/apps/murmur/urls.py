from django.urls import path
from . import views

app_name = 'murmur'

urlpatterns = [
    path('list', views.MurmurList.as_view(), name='murmur_list'),
    path('detail', views.MurmurDetail.as_view(), name='murmur_detail'),
    path('edit', views.MurmurEdit.as_view(), name='murmur_edit'),
    path('post', views.MurmurPost.as_view(), name='murmur_post'),
]
