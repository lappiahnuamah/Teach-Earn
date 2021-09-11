from django.shortcuts import render
from django.shortcuts import redirect, render

from .models import Videos


def displayAndUpload_video(request):
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
    
    
    if request.method == 'POST': 
        title = request.POST['title']
        video = request.POST['video']
        
        content = Videos(title=title,video=video)
        content.save()
        return redirect('videos')
    
    return render(request,'videos.html', context)