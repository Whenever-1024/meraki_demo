from django.http import request
from django.shortcuts import render,redirect
from django.views import View


class DashboardView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"

        return render(request, 'dashboard/dashboard.html',greeting)
