"""
    urls
    ~~~

    URL mappings for the user API.

    :author: dilless(Huangbo)
    :date: 2022/8/24
"""

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
