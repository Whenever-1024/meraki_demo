from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview.as_view(), name='demo'),
    path('getData', views.homeview.as_view(), name='getData'),
    path('ConfigVPN/<str:ip>', views.homeview.as_view(), name='ConfigVPN'),
]
