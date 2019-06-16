from django.conf.urls import url

from ..rest_api import views

urlpatterns = [
    url(r'register/', views.register),
    url(r'token/', views.token),
    url(r'token/refresh/', views.refresh_token),
    url(r'token/revoke/', views.revoke_token),
]