from django.shortcuts import render,redirect, HttpResponseRedirect,get_object_or_404
from .forms import Signupform , Signinform 
from . models import Userprofile,student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import Http404


def insertdata(request):
    if request.user.is_authenticated:
        data=student.objects.all()
        context={"data":data}
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            age=request.POST.get('age')
            print(name,email,age)
            query=student(name=name,email=email,age=age)
            query.save()
            return redirect("insertdata")
        return render(request,'app/student.html',context)
    else:
        messages.error(request,"login first")
        return redirect("/")




def updatedata(request,id):
    d=student.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        
        
        edit=student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.save()
        return redirect("insertdata")
      

    return render(request,'app/edit.html',{"d":d})


def deletedata(request,id):
    try:
        d=student.objects.get(id=id)
        d.delete()
        return redirect("insertdata")
    except student.DoesNotExist:
        messages.error(request,"student Does Not Exist")
        return redirect("insertdata")
      






   
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

def edit_user(request,id):

    user = User.objects.get(id=id)
    return render(request,"app/edit-user.html",{"user":user})


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


def update_user(request, id):
    user = User.objects.get(id=id)

    if request.method == "POST":
        form = Signupform(request.POST, instance = user)

        if form.is_valid():
            form.save()
            # Process valid form data here

            return redirect("user-list")
    else:
        form = Signupform(instance=user)

    return render(request, "app/edit-user.html", {"form": form, "user": user})
    