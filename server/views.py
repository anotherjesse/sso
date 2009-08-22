from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import django.contrib.auth

def login(request):
    if request.POST:
        user = User.objects.get(username__exact=request.POST['username']) # TODO: check password as well ;)
        response = HttpResponseRedirect('/')
        response.set_cookie('sso', str(user.id) + '|SIGNATURE') # TODO: really sign it
        return response

    return render_to_response('login.html', {})

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('sso')
    return response

def status(request):
    return HttpResponse('SERVER: hi %s' % request.user)
    