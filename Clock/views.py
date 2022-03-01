from django.shortcuts import render
from django.views import View


class ClockView(View):
    def get(self, request):
        return render(request, "Clock.html")
