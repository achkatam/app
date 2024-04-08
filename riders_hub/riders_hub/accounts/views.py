from django.contrib.auth import get_user_model
from rest_framework import generics as auth_views, permissions
from rest_framework.authtoken import views as api_token_views

from riders_hub.accounts.serializers import RiderUserCreateSerializer

UserModel = get_user_model()


class CreateUserApiView(auth_views.CreateAPIView):
    serializer_class = RiderUserCreateSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]


class LoginUserApiView(api_token_views.ObtainAuthToken):
    permission_classes = [permissions.AllowAny]


class LogoutUserApiView:
    permission_classes = [permissions.IsAuthenticated]
