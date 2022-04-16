from mimetypes import init
from django import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.conf import settings
from requests import request
import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail
import json

# from .models import CommitteeMember
from authentication.models import Profile
from website.models import Facility, Product
from .models import Apartment, Price
from .forms import CommitteMemberForm, FacilityForm, UpdateCommitteMemberForm

register = template.Library()


def search_members(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        members = Profile.objects.filter(name__contains=searched)
        # print(members)
        for member in members:
            print(member, "memmm")
        return render(
            request,
            "search_member.html",
            {"searched": searched, "members": members},
        )
    else:
        return render(request, "search_member.html", {})



class HomeView(ListView):
    model = Profile
    template_name = "home.html"
    ordering = ["-timestamp"]

    def get_queryset(self):
        try:
            apartment_id = self.request.user.profile.apartment_id
            queryset = Profile.objects.filter(apartment_id=apartment_id)
        except:
            queryset = Profile.objects.all()

        return queryset


class CommitteeMemberDetailView(DetailView):
    model = Profile
    template_name = "committee_member.html"


class AddCommitteMemberView(CreateView):
    model = Profile
    form_class = CommitteMemberForm
    template_name = "add_member.html"
    # fields = ('name','contact_number','emergency_contact_number', 'flat_number', 'blood_group', 'family_members')


class UpdateCommitteMemberView(UpdateView):
    model = Profile
    form_class = UpdateCommitteMemberForm
    template_name = "update_member.html"
    # fields = ('contact_number','emergency_contact_number', 'flat_number', 'blood_group', 'family_members')

class CreateFacilityView(CreateView):

    model = Facility
    form_class = FacilityForm
    template_name = "create_facility.html"
    success_url = reverse_lazy("facility")

    def form_valid(self, form):
        apartment_id = self.request.user.profile.apartment_id
        form.instance.apartment = Apartment.objects.get(pk=apartment_id)
        return super().form_valid(form)
    



def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


class FacilityView(ListView):
    model = Facility
    template_name = "facility.html"
    
    def get_queryset(self):
        try:
            apartment_id = self.request.user.profile.apartment_id
            queryset = Facility.objects.filter(apartment_id=apartment_id)
        except:
            queryset = Facility.objects.all()
        
        return queryset


class FacilityDetail(DetailView):
    model = Facility
    template_name = "facility_detail.html"
    

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Facility.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items = [
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)




class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        prices = Facility.objects.filter(product=product)
        context = super(
            ProductLandingPageView,
            self
        ).get_context_data(**kwargs)

        context.update({
            "product": product,
            "prices": prices
        })
        return context


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session["customer_details"]["email"]
        line_items = stripe.checkout.Session.list_line_items(session["id"])

        stripe_price_id = line_items["data"][0]["price"]["id"]
        price = Price.objects.get(stripe_price_id=stripe_price_id)
        product = price.product

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. The URL is: {product.url}",
                recipient_list=[customer_email],
                from_email="your@email.com"
            )

    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

    stripe_customer_id = intent["customer"]
    stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

    customer_email = stripe_customer['email']
    price_id = intent["metadata"]["price_id"]

    price = Price.objects.get(id=price_id)
    product = price.product

    send_mail(
        subject="Here is your product",
        message=f"Thanks for your purchase. The URL is {product.url}",
        recipient_list=[customer_email],
        from_email="your@email.com"
    )
    return HttpResponse(status=200)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            price = Price.objects.get(id=self.kwargs["pk"])
            intent = stripe.PaymentIntent.create(
                amount=price.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "price_id": price.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

class CustomPaymentView(TemplateView):
    template_name = "custom_payment.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        prices = Price.objects.filter(product=product)
        context = super(CustomPaymentView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context