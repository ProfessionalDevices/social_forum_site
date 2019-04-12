from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('user/<username>/', views.userProfileView, name='user_profile'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('cerca/', views.cerca, name='funzione_cerca'),
]
