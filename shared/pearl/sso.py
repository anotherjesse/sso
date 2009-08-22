from django.contrib.auth.models import User, AnonymousUser
from django.conf import settings
import django_pipes as pipes



def fetch_user(user_id):
    """
    download a json blob of the user object from the master auth server
    """
    class UserApi(pipes.Pipe):
        uri = "http://localhost/api/user.json"

        @staticmethod
        def fetch(user_id):
            return UserApi.objects.get({'id': user_id})

    return UserApi.fetch(user_id).items

def load_user(user_id):
    """
    load the user from the local database, if it doesn't exist clone
    the user from the master auth server
    """
    
    # FIXME: load_user should re-download user info if it is stale
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        data = fetch_user(user_id)
        user = User(id=data['id'], username=data['username'], email=data['email'])
        user.save()
    return user

# FIXME: session invalidation should not be lazy
class LazyUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            try:
                user_id = request.COOKIES['sso'].split('|')[0]
                # FIXME: verify signature
                user = load_user(user_id)
            except Exception, e:
                user = AnonymousUser()
            # FIXME: if session already had an SSO_USER and it is different
            #        then a new session should be created
            request._cached_user = user
        return request._cached_user

class AuthMiddleware(object):
    def process_request(self, request):
        request.__class__.user = LazyUser()
        return None
