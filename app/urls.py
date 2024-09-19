from django.urls import path

from app import views

urlpatterns = [
    path('',views.test,name='test'),
    path('index',views.index,name='index'),
    path('dash',views.index_dashboard,name='dash'),
]