from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from posts.models import Posts




# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
                  {"current_time": datetime.now(),
                   "posts": Posts.objects.all(),
                   "num_posts": Posts.objects.count()})