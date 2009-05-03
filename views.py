from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from projects.models import Project
def index(request):
    return render_to_response('index.html',{

        'project_list': Project.objects.all(),

        'user_list': User.objects.all(),
    })
