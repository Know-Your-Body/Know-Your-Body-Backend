from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

from know_your_body_backend.users import views


users_api_urls = [
    url(r'signup', views.SignUpUserView.as_view()),
    url(r'login', authtoken_views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
