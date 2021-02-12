from django.urls import path
from dashboard.views import TestView


urlpatterns = [
    path('test/', TestView.as_view()),
]
