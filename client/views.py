from django.http import HttpResponse

def status(request):
    return HttpResponse('CLIENT: hi %s' % request.user)
