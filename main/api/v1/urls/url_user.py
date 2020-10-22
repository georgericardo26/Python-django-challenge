from django.urls import path, re_path, include
from main.api.v1.views import view_user as views


url_github = [

    path('list',
         views.UserList.as_view(),
         name='user_list'),

    path('<slug:username>/',
         views.UserRetrieveAPIView.as_view(),
         name='user_retrieve_by_username'),

    path('<slug:username>/repos',
         views.UserRetrieveAllReposAPIView.as_view(),
         name='user_retrieve_repos_by_username'),

    path('create',
         views.UserSaveAPIView.as_view(),
         name='user_save'),
]

url_local = [

    path('local/list',
         views.UserListLocalAPIView.as_view(),
         name='user_local_list'),

    path('local/<slug:login>/',
         views.UserRetrieveLocalAPIView.as_view(),
         name='user_local_retrieve_by_username'),

]

urlpatterns = url_github + url_local