from .models import AcademicTerm, AcademicSession, SiteConfig

def site_defaults(request):
    try:
        current_session = AcademicSession.objects.get(current=True)
        current_term = AcademicTerm.objects.get(current=True)
    except (AcademicSession.DoesNotExist, AcademicTerm.DoesNotExist) as ex:
        current_session = None
        current_term = None
    vals = SiteConfig.objects.all()
    contexts = {
      "current_session": current_session.name if current_session else None,
      "current_term": current_term.name if current_term else None
    }
    for val in vals:
        contexts[val.key] = val.value

    return contexts
