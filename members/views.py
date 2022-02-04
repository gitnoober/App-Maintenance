from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView
from .forms import CommitteMemberModelForm
from django.contrib import messages
from rest_framework.views import APIView
from .models import CommitteeMember
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import AllMembersSerializer
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def check_if_member(request):
    if request.user.is_authenticated:
        queryset = CommitteeMember.objects.filter(user=request.user)
        if queryset.exists():
            return True
        else:
            return False
    else:
        # return response("You need to logged in to be a member!")
        return False



class CommiteeMemberFormView(FormView):
    form_class = CommitteMemberModelForm
    template_name = 'members/main.html'

    def get_success_url(self): # redirect to home page 
        return "authentication/index.html"
        # print(self.request.path)
        # return self.request.path

    def form_valid(self,form):
        form.save()
        messages.add_message(self.request, messages.INFO,'Saved successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Oops..something went wrong')
        return super().form_invalid(form)
    
# search member view
class AdminMemberView(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, request,format=None):
        queryset = CommitteeMember.objects.all().values()
        return JsonResponse({"models_to_return": list(queryset)})
        

class CommiteeMemberChangeView(CreateView):
    form_class = UserChangeForm
    template_name = 'members/edit_profile.html'
    def get_success_url(self): # redirect to home page 
        return "authentication/index.html"