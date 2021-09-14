from django.urls import path
from . import views

app_name = 'scraps'

urlpatterns = [
    path('', views.EventsList, name='index'),
    path('post', views.PostEvent, name='event_post'),
    path('detail/<int:id>/', views.EventDetail, name='event_detail'),

]
