from django.http import HttpResponseForbidden
from datetime import datetime, time


class TimeRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()

        start_time = time(12, 0)
        end_time = time(13, 50)

        if not (start_time <= current_time < end_time):
            return HttpResponseForbidden(f"Access is allowed only between {start_time} and {end_time}.")

        response = self.get_response(request)
        return response
