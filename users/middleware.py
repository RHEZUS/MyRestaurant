from django.http import HttpResponseForbidden
from django.http import HttpResponseServerError

class AdminRoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.role != 'admin':
            return HttpResponseForbidden("You do not have the required admin role.")
        if self.get_response:
            response = self.get_response(request)
            return response #self.get_response(request)
        else:
            # If get_response is None, return a 500 Internal Server Error
            return HttpResponseServerError("Internal Server Error: get_response attribute is not callable.")
