import json

import requests
from django.core.paginator import Paginator
from django.urls import reverse
from rest_framework.filters import SearchFilter
from django.db.models import Q
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from core.api.v1.serializers.serializer_user import UserSerializer, UserRetrieveSerializer
from main.api.v1.base import reverse_url, ROOT_ENDPOINT
# from core.models import User
from main.api.v1.mixins import MultipleFieldLookupMixin
from main.api.v1.serializers.serializer_user import UserSerializer
from main.models import User, Repository

PERMISSION_CLASSES = (AllowAny,)


