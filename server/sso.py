class LazyUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            from django.contrib.auth.models import User, AnonymousUser
            try:
                user_id = request.COOKIES['sso'].split('|')[0]
                # TODO: verify signature
                # TODO: move the user object if it doesn't exist in the local DB
                user = User.objects.get(id__exact=request.COOKIES['sso']) or AnonymousUser()
            except KeyError:
                user = AnonymousUser()
            # TODO: if session already had an SSO_USER and it is different
            #       then a new session should be created
            request._cached_user = user
        return request._cached_user

class SSOMiddleware(object):
    def process_request(self, request):
        request.__class__.user = LazyUser()
        return None
