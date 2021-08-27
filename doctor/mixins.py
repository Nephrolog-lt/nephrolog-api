from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View

from core.models import Doctor


class UserIsDoctorMixin(UserPassesTestMixin, View):
    def test_func(self):
        user = self.request.user

        return user.is_authenticated and Doctor.objects.filter(user=user).exists()

    # def handle_no_permission(self):
    #     return redirect('doctor:index')
