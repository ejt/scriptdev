from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from projects.models import Project
from contact_form.forms import AkismetContactForm

def index(request):
    if request.method == "POST":
        # User authentication
        auth_form = AuthenticationForm(data = request.POST)

        if auth_form.is_valid():
            user = auth_form.get_user()

            if user.is_active:
                login(request, user)

        # Contact form handling
        contact_form = AkismetContactForm(request = request, data = request.POST)

        if contact_form.is_valid():
            contact_form.save()
    else:
        auth_form = AuthenticationForm()
        contact_form = AkismetContactForm(request = request)

    return render_to_response('index.html',{
        'auth_form': auth_form,
        'contact_form': contact_form,
        'project_list': Project.objects.all(),
        'user_list': User.objects.all().order_by('first_name')
    }, context_instance = RequestContext(request))
