from django.shortcuts import render
from django.views import View

from LIT_UI.settings import ALLOWED_HOSTS, get_ip_address


class ClockView(View):
    def get(self, request):
        print(ALLOWED_HOSTS[0])
        return render(request, "Clock.html", {"IP", get_ip_address()})
