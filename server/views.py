from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import django.contrib.auth

def login(request):
    if request.POST:
        user = User.objects.get(username__exact=request.POST['username'])
        response = HttpResponseRedirect('/')
        response.set_cookie('sso', str(user.id))
        return response

    return render_to_response('login.html', {})

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('sso')
    return response

def status(request):
    user = User.objects.get(id__exact=request.COOKIES['sso'])
    return HttpResponse('SERVER: hi %s' % user)
    