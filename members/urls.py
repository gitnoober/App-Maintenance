from django.urls import path

from .views import (
    AdminMemberView,
    CommiteeMemberChangeView,
    CommiteeMemberFormView,
)

app_name = "members"

urlpatterns = [
    path("add/", CommiteeMemberFormView.as_view(), name="member-add"),
    path(
        "edit_profile/",
        CommiteeMemberChangeView.as_view(),
        name="edit_profile",
    ),
    path("all-members/", AdminMemberView.as_view(), name="all-members"),
]
