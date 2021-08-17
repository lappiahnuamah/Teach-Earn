from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def index(request):
    return render(request, 'registration/base.html', {})

    
def about(request):
    return render(request, 'registration/about.html', {})


def login(request):
    return render(request, 'registration/login.html', {})


def register(request):
    return render(request, 'registration/register.html', {})


def forgotten(request):
    return render(request, 'registration/forgotten_password.html', {})