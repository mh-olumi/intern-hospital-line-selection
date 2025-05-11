#Session model stores the session data
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
from .models import Members
import datetime
import threading
from pytz import timezone
from django.urls import reverse


class AutoRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.redirect_time = datetime.time(hour=22, minute=23)  # Set the redirect time (in this example, 6:00 PM)
        self.redirect_url = 'index'  # Replace 'main-page' with the URL name of your main page view
        self.check_time_thread = threading.Thread(target=self.check_time)
        self.check_time_thread.daemon = True
        self.check_time_thread.start()

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def check_time(self):
        while True:
            request = getattr(self.thread_local, 'request', None)
            if request:
                if request.path == '/line/select/' or request.path == '/select/':
                    if self.should_redirect():
                        # Redirect to the main page URL
                        redirect_url = '/' + self.redirect_url + '/'  # Assuming the main page URL is '/main-page/'
                        return redirect(redirect_url)
                    # Check every second
                threading.Event().wait(1)
            threading.Event().wait(1)

    def should_redirect(self):
        current_time = datetime.datetime.now().time()
        return current_time >= self.redirect_time
    
    thread_local = threading.local()

            
 

class OneSessionPerUserMiddleware:
    # Called only once when the web server starts
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            stored_session_key = request.user.logged_in_user.session_key

            # if there is a stored_session_key  in our database and it is
            # different from the current session, delete the stored_session_key
            # session_key with from the Session table
            if stored_session_key and stored_session_key != request.session.session_key:
                try:
                    Session.objects.get(session_key=stored_session_key).delete()
                except:
                    pass
                

            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)

        # This is where you add any extra code to be executed for each request/response after
        # the view is called.
        # For this tutorial, we're not adding any code so we just return the response

        return response