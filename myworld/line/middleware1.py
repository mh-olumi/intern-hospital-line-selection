# middleware.py
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class SingleLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            current_session_key = request.session.session_key

            try:
                other_sessions = Session.objects.filter(
                    expire_date__gt=timezone.now(),
                    session_data__contains=f'"_auth_user_id":{request.user.id}'
                ).exclude(session_key=current_session_key)

                for session in other_sessions:
                    session_data = session.get_decoded()
                    user_id = session_data.get('_auth_user_id')
                    if user_id == request.user.id:
                        session.delete()
            except Exception as e:
                # Handle exceptions, log, or raise as needed
                pass

        return response
