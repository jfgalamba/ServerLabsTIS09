__all__ = (
    'requires_authentication',
    'requires_unauthentication',
    'get_current_user',
    'set_auth_cookie',
    'get_auth_from_cookie',
    'delete_auth_cookie',
)


from hashlib import sha512
from fastapi import HTTPException

from fastapi.requests import Request
from fastapi.responses import Response
from fastapi import status

from data.models import Student
from services import student_service
from common.fastapi_utils import global_request


SECRET_KEY = '8e10d234a1f8eb6f9dd6dfc3a325a0613ad2e620e5b8844cb011470492422bee'
AUTH_COOKIE_NAME = 'user_id'
SESSION_COOKIE_MAX_AGE = 86400_00    # in seconds (~100 days)
# SESSION_COOKIE_MAX_AGE = 30    # in seconds


def requires_authentication():
    if not get_current_user():
        raise HTTPUnauthorizedAccess(detail = 'This area requires authentication.')
#:

def requires_unauthentication():
    if get_current_user():
        raise HTTPUnauthenticatedOnly(detail = 'This is a public area only.')
#:

# NOTE: These classes won't be suffixed with 'Exception' or 'Error',
# because they aren't necessarily exceptions/errors. They are used for
# control flow. Yes, exceptions shouldn't be used for this, but there's
# no clean way to protect access to a view without raising an exception.
# Besides, using exceptions as a control flow mechanism is often used in
# Python built-ins and libraries (eg, StopIteration is raised when an
# iterator is done).

class HTTPUnauthorizedAccess(HTTPException):
    def __init__(self, *args, **kargs):
        super().__init__(status_code = status.HTTP_401_UNAUTHORIZED, *args, **kargs)
#:

class HTTPUnauthenticatedOnly(HTTPUnauthorizedAccess):
    pass
#:

def get_current_user() -> Student | None:
    if student_id := get_auth_from_cookie(global_request.get()):
        return student_service.get_student_by_id(student_id)
    return None
#:

def set_auth_cookie(response: Response, user_id: int):
    cookie_value = f'{user_id}:{hash_cookie_value(str(user_id))}'
    response.set_cookie(
        AUTH_COOKIE_NAME, 
        cookie_value, 
        secure = False, 
        httponly = True, 
        samesite = 'lax',
        max_age = SESSION_COOKIE_MAX_AGE,
    )
#:

def get_auth_from_cookie(request: Request) -> int | None:
    if not (cookie_value := request.cookies.get(AUTH_COOKIE_NAME)):
        return None

    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None

    user_id, hash_value = parts
    hash_value_check = hash_cookie_value(str(user_id))
    if hash_value != hash_value_check:
        print("Warning: hash mismatch. Invalid cookie value!")
        return None

    return int(user_id) if user_id.isdigit() else None
#:

def delete_auth_cookie(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)
#:

def hash_cookie_value(value: str) -> str:
    return sha512(f'{value}{SECRET_KEY}'.encode('utf-8')).hexdigest()
#:
