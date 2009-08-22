from django.http import HttpResponseRedirect, HttpResponse
import django.contrib.auth

def logout(request, next_page=None):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(next_page or '/')

def status(request):
    return HttpResponse('hello: %s' % request.user)
    