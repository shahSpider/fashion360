from django.urls import path
from setup.views import homepage


urlpatterns = [
    path('', homepage)
]