from django.urls import path

from .views import (
    AddCommitteMemberView,
    CommitteeMemberDetailView,
    HomeView,
    UpdateCommitteMemberView,
    about,
    contact,
)

# app_name = "website"

urlpatterns = [
    # path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path(
        "member/<int:pk>",
        CommitteeMemberDetailView.as_view(),
        name="member-detail",
    ),
    path("add_member", AddCommitteMemberView.as_view(), name="member-add"),
    path(
        "member/edit/<int:pk>",
        UpdateCommitteMemberView.as_view(),
        name="member-edit",
    ),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
]
