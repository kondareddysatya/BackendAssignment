from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        header = super().get_header(request)
        if header:
            return header.replace("Bearer", "JWT", 1)
        return header