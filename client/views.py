from django.contrib.auth.models import User
from django.http import HttpResponse

def status(request):
    return HttpResponse('CLIENT: hi %s' % request.user)
