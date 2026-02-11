from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from app.users.models import User
from app.users.serializers import RegisterSerializers, UserProfileSerializers

class RegisterAPI(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers

class ProfileAPI(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [IsAuthenticated,]