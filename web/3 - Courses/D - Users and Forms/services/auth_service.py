
from hashlib import sha512

from fastapi import Request, Response


AUTH_COOKIE_NAME = 'user_id'
SECRET_KEY = '8e10d234a1f8eb6f9dd6dfc3a325a0613ad2e620e5b8844cb011470492422bee'

def set_auth_cookie(response: Response, user_id: int):
    cookie_value = f'{user_id}:{hash_cookie_value(str(user_id))}'
    response.set_cookie(
        AUTH_COOKIE_NAME,
        cookie_value,
        secure = False,      # True -> enviadas apenas por HTTPS
        httponly = True,
        samesite = 'lax',
    )
#:

def get_auth_from_cookie(request: Request) -> int | None:
    if not (cookie_value := request.cookies.get(AUTH_COOKIE_NAME)):
        return None

    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None
    
    user_id, hash_value = parts
    hash_value_check = hash_cookie_value(user_id)
    if hash_value != hash_value_check:
        print("Warning: hash mismatch. Invalid cookie value!")
        return None

    return int(user_id) if user_id.isdigit() else None
#:

def delete_auth_cookie(response: Response): 
    response.delete_cookie(AUTH_COOKIE_NAME)
#:

def hash_cookie_value(value: str) -> str:
    # bytes 
    return sha512(f'{value}{SECRET_KEY}'.encode('utf-8')).hexdigest()
#:
