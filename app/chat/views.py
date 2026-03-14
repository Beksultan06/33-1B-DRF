from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.chat.authentication import QueryParamJWTAuthentication
from app.chat.models import ChatRoom
from app.chat.serializers import (
    ChatRoomCreateSerializer,
    ChatRoomSerializer
)

token_parameter = openapi.Parameter(
    "token",
    openapi.IN_QUERY,
    description="JWT access token. Example : ?token=<token>",
    type=openapi.TYPE_STRING,
    required=True    
)

