from django.urls import path
from . import views

urlpatterns = [
    path('', views.nested_index, name='nested-index'),
    path('info/', views.nested_info, name='nested-info'),
    path('user/<str:username>/', views.nested_user, name='nested-user'),
]
