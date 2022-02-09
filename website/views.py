from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CommitteMemberForm, UpdateCommitteMemberForm
from .models import CommitteeMember


# Create your views here.
# def home(request):
#     return render(request, "home.html", {})
class HomeView(ListView):
    model = CommitteeMember
    template_name = "home.html"
    ordering = ["-added_on"]
    # ordering = ['-id']


class CommitteeMemberDetailView(DetailView):
    model = CommitteeMember
    template_name = "committee_member.html"


class AddCommitteMemberView(CreateView):
    model = CommitteeMember
    form_class = CommitteMemberForm
    template_name = "add_member.html"
    # fields = ('name','contact_number','emergency_contact_number', 'flat_number', 'blood_group', 'family_members')


class UpdateCommitteMemberView(UpdateView):
    model = CommitteeMember
    form_class = UpdateCommitteMemberForm
    template_name = "update_member.html"
    # fields = ('contact_number','emergency_contact_number', 'flat_number', 'blood_group', 'family_members')


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})
