from django.urls import path

from .views import (
    PasswordsChangeView,
    ShowProfilePageView,
    UserEditView,
    UserRegisterView,
    password_success,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    # path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path("password/", PasswordsChangeView.as_view(), name="password_change"),
    path("password_success", password_success, name="password_success"),
    path(
        "<int:pk>/profile",
        ShowProfilePageView.as_view(),
        name="show_profile_page",
    ),
]
