from django.http import HttpRequest


def doctor_patients(request: HttpRequest):
    if hasattr(request, 'doctor_patients'):
        return {
            'doctor_patients': request.doctor_patients,
        }

    return {}
