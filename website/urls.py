from django.urls import path

from .views import (
    AddCommitteMemberView,
    CommitteeMemberDetailView,
    HomeView,
    UpdateCommitteMemberView,
    FacilityView,
    FacilityDetail,
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView,
    StripeIntentView,
    CustomPaymentView,
    CreateFacilityView,
    about,
    contact,
    search_members,
    stripe_webhook
)

# app_name = "website"

urlpatterns = [
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
    path("facility", FacilityView.as_view(), name="facility"),
    path("facility/<int:pk>", FacilityDetail.as_view(),name="facility-detail"),
    

    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("search-member", search_members, name="search-members"),

    path('cancel/', CancelView.as_view(), name="cancel"),
    path('success/', SuccessView.as_view(), name="success"),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('product-landing-page', ProductLandingPageView.as_view(),name="landing"),
    path('webhooks/stripe/', stripe_webhook,name="stripe-webhook"),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('custom-payment/', CustomPaymentView.as_view(), name='custom-payment'),
    path('create-facility/',CreateFacilityView.as_view(), name="create-facility")

]
