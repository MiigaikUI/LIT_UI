from django.shortcuts import render
from django.views import View

from LIT_UI.settings import ALLOWED_HOSTS, get_ip_address


class ClockView(View):
    def get(self, request):
        return render(request, "Clock.html", {"IP": ALLOWED_HOSTS[0],})
