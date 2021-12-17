from django.contrib import admin
from django.urls import include, path
from meraki_demo import views

urlpatterns = [
    path('',views.DashboardView.as_view(),name='dashboard'),
    path("demo/", include('demo.urls')),
    path("admin/", admin.site.urls)
]
