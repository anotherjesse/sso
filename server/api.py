from wapi.responses import SingleSerializableResponse
from wapi.decorators import required_parameter, readonly
from wapi.shortcuts import get_object_or_empty

from django.contrib.auth.models import User

class UserApi(object):
    @readonly
    @required_parameter('id', int, 'id of user')
    def user(self, request, params):
        user = get_object_or_empty(User, id=params['id'])
        user.password = None # don't send the password
        return SingleSerializableResponse(user)
