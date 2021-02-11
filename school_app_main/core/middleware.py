from .models import AcademicTerm, AcademicSession

class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            current_session = AcademicSession.objects.get(current=True)
            current_term = AcademicTerm.objects.get(current=True)
        except (AcademicSession.DoesNotExist, AcademicTerm.DoesNotExist) as ex:
            current_session = None
            current_term = None

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response
