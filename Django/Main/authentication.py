from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from jwt import InvalidTokenError

class MicroserviceUser:
    def __init__(self, user_id, role=None):
        self.id = user_id
        self.role = role
        self.is_authenticated = True

    def __str__(self):
        return str(self.id)

class MicroserviceJWTAuthentication(BaseAuthentication):

    def authenticate(self, request): 
        auth_header = request.COOKIES.get("access_token")
 
        if not auth_header:
            return None  

        try:
            token = auth_header  

            payload = jwt.decode(
                token,
                settings.JWT_PUBLIC_KEY,
                algorithms=settings.SIMPLE_JWT['ALGORITHM'] 
            )

        except InvalidTokenError:
            raise AuthenticationFailed("Invalid or expired token")

        if "sub" not in payload:
            raise AuthenticationFailed("Invalid token payload")
 
        user = MicroserviceUser(
            user_id=payload.get("sub"),
            role=payload.get("role"),
        )

        return (user, None)
