from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

# from website.models import CommitteeMember
from authentication.models import Profile

from .forms import (
    EditProfileForm,
    PasswordChangedForm,
    SignUpForm,
    UpdateProfileForm,
    UpdateUserForm,
)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST,instance=request.user.profile)
#         print(user_form.is_valid(), profile_form.is_valid)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='home')
#         else:
#             user_form = UpdateUserForm(instance=request.user)
#             profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'registration/profile.html', {'user_form': user_form, 'profile_form': profile_form})
@login_required
def profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, instance=request.user.profile
        )  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect("home")
    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args["form"] = form
        args["profile_form"] = profile_form
        # print(args)
        return render(request, "registration/profile.html", args)


class ShowProfilePageView(DetailView):
    # model = CommitteeMember
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        # users = CommitteeMember.objects.all()
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(
            *args, **kwargs
        )
        # page_user = get_object_or_404(CommitteeMember, id=self.kwargs["pk"])
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangedForm
    # success_url = reverse_lazy("home")
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, "registration/password_success.html", {})


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


# # Create your views here.
# def home(request):
#     val = check_if_member(request)
#     print("pppss")
#     return render(request, "website:home.html", {"context": val})


# def signup(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         fname = request.POST["fname"]
#         lname = request.POST["lname"]
#         pass1 = request.POST["pass1"]
#         pass2 = request.POST["pass2"]

#         if pass1 != pass2:
#             messages.error(request, "Your passwords are mismatched")
#             return redirect("signup")

#         myuser = User.objects.create_user(username, fname, pass1)
#         myuser.firest_name = fname
#         myuser.last_name = lname

#         myuser.save()

#         messages.success(
#             request, "Your Account has been successfully created."
#         )

#         return redirect("signin")

#     return render(request, "authentication/signup.html")


# def signin(request):

#     if request.method == "POST":
#         username = request.POST["username"]
#         pass1 = request.POST["pass1"]

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             # fname = user.first_name
#             val = check_if_member(request)
#             # print("render")
#             # return render(
#             #     # request, "authentication/index.html", {"context": val}
#             #     request, "home",{"context": val}
#             # )
#             return HttpResponseRedirect(reverse('home', kwargs={"context": val}))


#         else:
#             messages.error(request, "Add Valid credentials!")
#             return redirect("home")
#             # return redirect("website:home")

#         # return redirect("website:home")

#     print("ppp")
#     return render(request, "authentication/signin.html")
#     # return render(request, "website/home.html.html")


# def signout(request):
#     logout(request)
#     messages.success(request, "Logged out Successfully!")
#     return redirect("website:home")
