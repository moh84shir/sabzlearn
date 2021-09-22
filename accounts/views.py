from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    template_name = 'accounts/login.html'
    context = {}
    form_class = LoginForm

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')

        login_form = self.form_class(request.POST or None)
        self.context['login_form'] = login_form
        return render(self.request, self.template_name, self.context)

    def post(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        login_form = self.form_class(request.POST or None)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('/')

        self.context['login_form'] = login_form
        return render(self.request, self.template_name, self.context)


class RegisterView(View):
    template_name = 'accounts/register.html'
    context = {}
    form_class = RegisterForm

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        register_form = self.form_class(request.POST or None)
        self.context['register_form'] = register_form
        return render(self.request, self.template_name, self.context)

    def post(self, request):
        if self.request.user.is_authenticated:
            return redirect('/')
        register_form = self.form_class(request.POST or None)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            email = register_form.cleaned_data.get('email')

            User.objects.create_user(username=username, password=password,
                                     email=email)

            return redirect('/accounts/login')

        self.context['register_form'] = register_form
        return render(self.request, self.template_name, self.context)


class LogOut(View):
    def get(self, request):
        logout(self.request)
        return redirect('/')
