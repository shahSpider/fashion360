from django.contrib import admin
from django.urls import path, include
from crm.views import *
from crm.views import CustomerListView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', CustomerListView, 'customers')

urlpatterns = [
    path('api/', include(router.urls)),
]