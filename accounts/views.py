from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics

from accounts.models import User
from accounts.serializers import UserSerializer


# API Views
class UserListCreateAPI(generics.ListCreateAPIView):
    """ Standard generic API view for listing and creating new User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"


# Django template views
def login_view(request):

    """ Login page.
     Contains a login form for authentication and authorization a User.
     Allows a User to enter a Home page if logged in successfully"""

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Validating a data as per given credentials
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Login or/and Password are not matching with any existed user")
            return render(request, 'accounts/login.html')

        else:
            # Login user. Change his network status to Online
            login(request, user)
            return redirect(reverse('core:home'))
    return render(request, 'accounts/login.html')


def registration_view(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirm = request.POST.get('password2')
        print(email, password)
        if password == password_confirm:
            new_user = get_user_model()(email=email, password=password)
            print(new_user)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, "Registered successfully!")
            return redirect(reverse("core:start"))
        else:
            print("No")
            return render(request, "accounts/registration.html")
    return render(request, "accounts/registration.html")
