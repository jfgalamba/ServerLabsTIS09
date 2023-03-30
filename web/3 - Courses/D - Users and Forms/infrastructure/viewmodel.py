from typing import Any

from services import auth_service
from infrastructure.middleware import global_request


__all__ = [
    'ViewModel',
]

class ViewModel(dict):
    def __init__(self, *args, **kargs):
        request = global_request.get()
        student_id = auth_service.get_auth_from_cookie(request)
        all = {
            'error': None,
            'error_msg': None,
            'user_id': student_id,
            'is_logged_in': bool(student_id),
        }
        all.update(kargs)
        super().__init__(*args, **all)
    #:

    def __getattr__(self, name: str) -> Any:
        return self[name]
    #:

    def __setattr__(self, name: str, value: Any) -> None:
        self[name] = value
    #:
#:

def base_viewmodel() -> dict:
    return {
        'error': None,
        'error_msg': None,
        'user_id': None,
        'is_logged_in': False,
    }
#:

def base_viewmodel_with(update_data: dict) -> dict:
    vm = base_viewmodel()
    vm.update(update_data)
    return vm
#:
