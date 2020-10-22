import json
import requests
from django.urls import reverse
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from main.api.v1.base import reverse_url, ROOT_ENDPOINT
from main.api.v1.mixins import MultipleFieldLookupMixin
from main.api.v1.serializers.serializer_user import UserSerializer
from main.models import User, Repository

PERMISSION_CLASSES = (AllowAny,)


class UserList(APIView):
    permission_classes = PERMISSION_CLASSES
    result = None
    obj = {}

    def get(self, request):

        params = {"since": request.GET.get("since", None)}
        request_api = requests.get(reverse_url("/users"), params=params)
        link = request_api.headers.get("Link")
        links = link.split(",")
        urls = list(map(
            lambda a: {
                "url": a.split(",")[0].replace(">", "").replace("<", "").split(";")
             },
            links
        ))
        absolute_url = request.build_absolute_uri(reverse('v1:user_list'))
        index = urls[0]["url"][0].find("since")
        next = "{}?{}".format(
            absolute_url,
            urls[0]["url"][0][index:]
        )
        first = "{}?{}".format(
            absolute_url,
            "since=1"
        )
        self.obj["next"] = next
        self.obj["first"] = first
        self.obj["result"] = request_api.json()

        if "save" in request.GET:
            list_users_save = {"data": []}
            i = 1
            n = int(request.GET["save"])
            while i <= n:
                list_users_save["data"].append(self.obj["result"][i])
                i += 1

            self.obj["result"] = requests.post(request.build_absolute_uri(reverse('v1:user_save')), json=list_users_save).json()

        return Response(self.obj)


class UserRetrieveAPIView(APIView):
    permission_classes = PERMISSION_CLASSES
    lookup_fields = ('username',)

    def get(self, request, username):

        request_api = requests.get("{}{}".format(
            reverse_url("/users/"),
            self.kwargs["username"]
        ))
        return Response(request_api.json())


class UserRetrieveAllReposAPIView(APIView):
    permission_classes = PERMISSION_CLASSES
    lookup_fields = ('username',)

    def get(self, request, username):

        request_api = requests.get("{}{}{}".format(
            reverse_url("/users/"),
            self.kwargs["username"],
            '/repos'
        ))
        return Response(request_api.json())


class UserSaveAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = PERMISSION_CLASSES
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        users = User.objects.bulk_create([User(id_user=x["id"],
                                              login=x["login"],
                                       node_id=x["node_id"]) for x in request.data["data"]
                                  if not User.objects.filter(login=x["login"]).exists()])
        if users:
            users_repos = []
            for item in users:
                request_api = requests.get(
                    request.build_absolute_uri(
                        reverse('v1:user_retrieve_repos_by_username',
                                kwargs={"username": item}
                                ))).json()

                repos = Repository.objects.bulk_create([Repository(id_repos=x["id"],
                                               name=x["name"],
                                               full_name=x["full_name"],
                                                           owner=User.objects.get(login=x["owner"]["login"])) for x in request_api
                                          if not Repository.objects.filter(id_repos=x["id"]).exists()])

                users_repos.append(repos)

            return Response(request.data["data"])
        raise serializers.ValidationError({"Error": "Already exists this user into Database"})


class UserListLocalAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = PERMISSION_CLASSES
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('id_user', 'login',)


class UserRetrieveLocalAPIView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = PERMISSION_CLASSES
    serializer_class = UserSerializer
    lookup_fields = ('login',)