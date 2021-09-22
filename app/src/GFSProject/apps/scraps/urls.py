from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'scraps'

urlpatterns = [
    # path('list', views.ScrapsList.as_view(), name='scraps_list'),
    # path('detail', views.ScrapsDetail.as_view(), name='scraps_detail'),
    # path('edit', views.ScrapsEdit.as_view(), name='scraps_edit'),
    # path('post', views.ScrapsPost.as_view(), name='scraps_post'),

    path('', views.EventsList, name='index'),
    path('post', views.PostEvent, name='event_post'),
    path('detail/<int:id>/', views.EventDetail, name='event_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
