from django.views import View
from django.shortcuts import render


class LoginView(View):

    """ Login View Definition """

    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass
