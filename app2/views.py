from django.shortcuts import render,redirect, HttpResponseRedirect
from .forms import Signupform , Signinform
from . models import Userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages



   
def about(request):
   if request.user.is_authenticated:
       return render(request,'app/about.html')
   else:
        
        messages.error(request,"to view the page please login first ")
        return redirect("signin")



def signin(request):


    if request.method == "POST":
        form = Signinform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('about')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request,"you have entered wrong username or password ! ")
                return redirect("signin")
    else:
        form = Signinform()
        return render(request, "app/signin.html", {"form": form})

def sign_out(request):
    logout(request)


    messages.success(request,"you have been succesfully LogOut ! ")
    return redirect('homepage')

   
    



def signup(request):
 
    if request.method == "POST":
        form = Signupform(request.POST)
        
        if form.is_valid():
            # Process valid form data here
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Creating a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            # You might want to log the user in here if needed
            
            return redirect("about")  # Redirect to a success page or any desired URL
    else:
        form = Signupform()
    
    
    return render(request, "app/signup.html", {"form": form})


def delete_user(request,id):

    user = User.objects.get(id=id)
    user.delete()
    return redirect("user-list")

def user_login(request):

    return render(request, 'app/user_login.html')


def homepage(request):
    return render(request,"app/logout.html")


def user_list(request):

    if request.user.is_authenticated:
      user=  User.objects.all()
      return render(request,"app/user-list.html",{'users':user})
    
    else:
        return redirect("signin")
    