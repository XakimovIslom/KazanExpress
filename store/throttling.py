from rest_framework.throttling import AnonRateThrottle
from datetime import datetime, time


class CustomHourlyThrottle(AnonRateThrottle):
    def allow_request(self, request, view):
        current_time = datetime.now().time()

        start_time = time(18, 0)
        end_time = time(20, 5)

        if not start_time <= current_time < end_time:
            return super().allow_request(request, view)

        return True
