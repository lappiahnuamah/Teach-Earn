from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from accounts.forms import Video_form
from django.http import HttpResponse, HttpRequest
from .models import Video



def courses(request):
    all = Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Uploaded Successfully</h1>")
    else:
        form=Video_form()
    return render(request, 'videos.html', {"form": form, "all":all})
