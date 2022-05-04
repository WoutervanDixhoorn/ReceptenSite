from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'username': str(user.username),
        'email': str(user.email),
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }