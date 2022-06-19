from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework import permissions
from django.contrib.auth import logout

from utils.customviewset import CustomModelViewSet
from utils.mixins import CustomResponseMixin, ExceptionMixin
from rest_framework.viewsets import GenericViewSet
from auth.views import CustomObtainAuthToken
from .serializers import UserSerializer
from .models import User



class UserViewSet(CustomModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    remove_field_list = ['password']
    http_method_names = ['get', 'patch', 'put', 'delete']

    def update(self, request, *args, **kwargs):
        return super().update(request, message="User details has been updated", *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, message="User has been deleted", *args, **kwargs)


class AuthViewSet(ExceptionMixin, CustomResponseMixin, CreateModelMixin, GenericViewSet):
    """
    API View for authentication of users which includes registration/login/logout
    """
    serializer_class = UserSerializer

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        data = {
            "status": "Success",
            "message": "User has been created successfully"
        }
        response = self.create(request)
        response.data = data
        return response

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        return CustomObtainAuthToken().as_view()(request=request._request)

    @action(methods=['POST', ], detail=False, permission_classes=[permissions.IsAuthenticated, ])
    def logout(self, request):
        request.user.auth_token.delete()
        logout(request)
        return self.custom_response(message="Successfully Logged Out")