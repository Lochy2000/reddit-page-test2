from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 

# Create your views here.

# ---------- login request ----------

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password) #authenticate user details with registerd accoutns

            if user is not None:
                login(request, user)
                messages.success(request,f"Welcome back, {username}!")
                return redirect ("posts:post_list")
    else:
        form = AuthenticationForm() # creates empty form for get request
    return render(request, "accounts/login.html", {"form": form}) # gets html login template


# ---------- Register request ----------

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): #authenticates data from the form
            user = form.save() #creates new user
            login(request, user) #log in new user
            messages.success(request,f"Welcome, {user.username}!")
            return redirect ("posts:post_list")
    else:
        form = UserCreationForm()
    return render (request, "accounts/register.html", {"form":form})

# ---------- Logout request ----------

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("posts:post_list")