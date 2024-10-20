from django.urls import path

from .views import user_view

app_name = "users"  # 앱 이름 설정

urlpatterns: list = [
    path("user/", user_view.UserListView.as_view(), name="user"),
]
