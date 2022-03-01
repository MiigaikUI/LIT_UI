from django.urls import path

from .views import ClockView

urlpatterns = [
    path('', ClockView.as_view()),
]
