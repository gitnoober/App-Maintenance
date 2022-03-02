from django import template
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

# from .models import CommitteeMember
from authentication.models import Profile

from .forms import CommitteMemberForm, UpdateCommitteMemberForm

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


# Create your views here.
# def home(request):
#     return render(request, "home.html", {})
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


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})
