from datetime import date

from fastapi import APIRouter, Request
from fastapi_chameleon import template
from fastapi import responses
from fastapi import status

from services import student_service
from services import auth_service
from data.models import Student
from infrastructure.common import (
    is_valid_name,
    is_valid_email,
    is_valid_password,
    is_valid_iso_date,
    form_field_as_str,
    MIN_DATE,
)
from infrastructure.viewmodel import ViewModel

router = APIRouter()

@router.get('/account/register')                            # type: ignore
@template()
async def register():
    return register_viewodel()
#:

def register_viewodel() -> ViewModel:
    return ViewModel(
        name = '',
        email = '',
        password = '',
        birth_date = '',
        min_date = MIN_DATE,
        max_date = date.today(),
        checked = False,
    )
#:

@router.post('/account/register')                            # type: ignore
@template(template_file='account/register.pt')
async def post_register(request: Request):
    vm = await post_register_viewmodel(request)
    if vm.error:
        return vm

    # TODO: fazer login do utilizador e memorizar o id do utilizador
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.set_auth_cookie(response, vm.new_student_id)
    return response
#:

async def post_register_viewmodel(request: Request) -> ViewModel:
    def is_valid_birth_date(birth_date: str) ->  bool:
        return (is_valid_iso_date(birth_date) 
                and date.fromisoformat(birth_date) >= MIN_DATE)
    #:

    form_data = await request.form()
    vm = ViewModel(
        name = form_field_as_str(form_data, 'name'),
        email = form_field_as_str(form_data, 'email'),
        password = form_field_as_str(form_data, 'password'),
        birth_date = form_field_as_str(form_data, 'birth_date'),
        new_student_id = None,
        min_date = MIN_DATE,
        max_date = date.today(),
        checked = False,
    )

    if not is_valid_name(vm.name):
        vm.error, vm.error_msg = True, 'Nome inválido!'
    #:
    elif not is_valid_email(vm.email):
        vm.error, vm.error_msg = True, 'Endereço de email inválido!'
    #:
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Senha inválida!'
    #:
    elif not is_valid_birth_date(vm.birth_date):
        vm.error, vm.error_msg = True, 'Invalid birth date!'
    #:
    elif student_service.get_student_by_email(vm.email):
        vm.error, vm.error_msg = True, f'Endereço de email {vm.email} já existe!'
    #:
    else:
        vm.error, vm.error_msg = False, ''
    #:

    if not vm.error:
        vm.new_student_id = student_service.create_account(
            vm.name,
            vm.email,
            vm.password,
            date.fromisoformat(vm.birth_date),
        ).id
    #:

    return vm
#:
@router.get('/account/login')                            # type: ignore
@template()
async def login():
    return login_viewodel()
#:

def login_viewodel():
    return ViewModel(
        email = '',
        password = '',
    )
#:

@router.post('/account/login')                            # type: ignore
@template(template_file='account/login.pt')
async def post_login(request: Request):  # TODO: tipo 
    vm = await post_login_viewmodel(request)

    if vm.error:
        return vm

    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.set_auth_cookie(response, vm.student_id)
    return response
#:

async def post_login_viewmodel(request: Request) -> ViewModel:
    form_data = await request.form()
    vm = ViewModel(
        email = form_field_as_str(form_data, 'email'),
        password = form_field_as_str(form_data, 'password'),
        student_id = None,
    )

    if not is_valid_email(vm.email):
        vm.error, vm.error_msg = True, 'Invalid user or password!'
    #:
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Invalid password!'
    #:
    elif not (student := 
            student_service.authenticate_student_by_email(vm.email, vm.password)):
        vm.error, vm.error_msg = True, 'User not found!'
    #:
    else:
        vm.error, vm.error_msg = False, ''
        vm.student_id = student.id
    #:
    return vm
#:

@router.get('/account/logout')                     # type: ignore
async def logout():
    response = responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    auth_service.delete_auth_cookie(response)
    return response
#:

@router.get('/account')                            # type: ignore
@template()
async def index():
    return account_viewmodel()
#:

def account_viewmodel() -> ViewModel:
    student = Student(
        id = 15_001,
        name = 'Alberto Antunes',
        email = 'alb@mail.com',
        password = 'abc',
        birth_date = date(1995, 2, 3),
    )
    return ViewModel(
        name = student.name,
        email = student.email,
    )
#:


