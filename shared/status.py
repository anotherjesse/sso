from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings

def app_info(request):
    def get_num():
        return request.session['number'] if 'number' in request.session else 0
        
    if 'inc' in request.GET and request.GET['inc']:
        request.session['number'] = get_num() + 1
        
    if request.user.is_authenticated():
        user_info = "Hi %s <a href='/logout'>logout</a>" % request.user
    else:
        user_info = "Anonymous: <a href='/login'>login</a>"
    
    counter_info = "App Session Info: %s<a href='?inc=true'>++</a>" % get_num()

    return HttpResponse('<b>%s</b><br>%s<br>%s' % (settings.SITE_NAME, user_info, counter_info))
