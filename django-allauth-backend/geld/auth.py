from rest_framework.authentication import SessionAuthentication

# Open auth
class EverybodyCanAuthentication(SessionAuthentication):
    def authenticate(self, request):
        return None
