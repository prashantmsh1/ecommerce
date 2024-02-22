from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import login_page, register_page, activate_account

urlpatterns = [
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
    path("activate/<str:email_token>", activate_account, name="activate_account"),
]
