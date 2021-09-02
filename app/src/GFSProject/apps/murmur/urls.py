from django.urls import path
from . import views
from django.urls import path
from django.urls import include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


app_name = 'murmur'

urlpatterns = [
    path('list', views.MurmurList.as_view(), name='murmur_list'),
    path('edit', views.MurmurEdit.as_view(), name='murmur_edit'),
    path('post/new', views.MurmurPost.as_view(), name='murmur_post'),
    path('post/<int:pk>/', views.MurmurDetail.as_view(), name='murmur_detail'),
    path('user/<str:name>', views.UserPostListView.as_view(), name='user-posts'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
