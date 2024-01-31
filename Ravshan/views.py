from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from Ravshan.form import UserRegistrationModelForm, UserLoginForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'Ravshan//home.html')


class UserRegisterView(View):
    def get(self, request):
        form = UserRegistrationModelForm()
        return render(request, "Ravshan//register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User registered successfully")
            form.save()
            return redirect('Ravshan/:login')
        else:
            return render(request, "Ravshan//register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "Ravshan//login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "User logged in successfully")
                return redirect("Ravshan/:home-page")
            else:
                messages.error(request, "Username or password is wrong")
                return redirect("Ravshan/:login")
        else:
            return render(request, "Ravshan//login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "Ravshan//logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User logged out successfully")
        return redirect('Ravshan/:home-page')


class UserAboutView(View):
    def get(self, request):
        return render(request, "Ravshan//about.html")


class UserHomeView(View):
    def get(self, request):
        return render(request, "Ravshan//home.html")


class UserPostDetailView(View):
    def get(self, request):
        return render(request, "Ravshan//post_detail.html")


class UserPostConfirmDeleteView(View):
    def get(self, request):
        return render(request, "Ravshan//post_confirm_delete.html")


class UserPostsView(View):
    def get(self, request):
        return render(request, "Ravshan/user_posts.html")


class UserPostsFormView(View):
    def get(self, request):
        return render(request, "Ravshan/post_form.html")

