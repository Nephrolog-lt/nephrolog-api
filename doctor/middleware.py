from django.http import HttpRequest, HttpResponse


class AssociateDoctorPatients:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if '/doctor/' not in request.get_full_path_info() or not request.user.is_authenticated:
            return self.get_response(request)

        from core.models import Doctor

        doctor = Doctor.get_doctor_by_user(request.user)

        if not doctor:
            return self.get_response(request)

        request.doctor_patients = doctor.get_patients()

        return self.get_response(request)
