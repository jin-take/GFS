from django.urls import path
from . import views
from GFSProject import views as topview

 
urlpatterns = [
    path('', topview.index, name='index'),
    path('accounts/profile/', views.Profile.as_view(), name='profile'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/logout/', views.Logout.as_view(), name='logout'),
    path('accounts/user_create/', views.UserCreate.as_view(), name='user_create'),
    path('accounts/user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('accounts/user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
]