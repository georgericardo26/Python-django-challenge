import os

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    id_user = models.IntegerField(primary_key=False, auto_created=False, null=False, blank=False)
    login = models.CharField(max_length=50, blank=False, null=False)
    node_id = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    deleted_in = models.DateField(auto_now=False, auto_now_add=False,
                                  null=True, blank=True)
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.login


class Repository(models.Model):
    id_repos = models.IntegerField(primary_key=False, auto_created=False, null=False, blank=False)
    name = models.CharField(max_length=60, blank=True, null=True)
    full_name = models.CharField(max_length=80, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='user_repositories',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    deleted_in = models.DateField(auto_now=False, auto_now_add=False,
                                  null=True, blank=True)
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name