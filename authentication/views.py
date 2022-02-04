from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from members.views import check_if_member
# Create your views here.
def home(request):
    val = check_if_member(request)
    return render(request, "authentication/index.html", {'context' : val})

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, "Your passwords are mismatched")
            return redirect('signup')

        
        myuser = User.objects.create_user(username,fname,pass1)
        myuser.firest_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            val = check_if_member(request)
            return render(request, "authentication/index.html", {"context" : val})

        else:
            messages.error(request, "Add Valid credentials!")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('home')
