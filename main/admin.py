from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (UserChangeForm, UserCreationForm)
from django import forms
from django.contrib.auth import get_user_model
from main.models import User, Repository

admin.site.register(User)
admin.site.register(Repository)

admin.site.site_header = "Oowlish API"
admin.site.site_title = "Oowlish API"
admin.site.index_title = "API Rest oowlish Github"