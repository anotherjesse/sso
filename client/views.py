from django.contrib.auth.models import User
from django.http import HttpResponse

def status(request):
    user = User.objects.get(id__exact=request.COOKIES['sso'])
    return HttpResponse('CLIENT: hi %s' % user)
