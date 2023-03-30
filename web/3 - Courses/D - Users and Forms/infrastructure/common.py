from datetime import date
import re
from typing import Any, Iterable
from fastapi import UploadFile
from fastapi.datastructures import FormData

__all__ = [
    'form_field_as_file',
    'form_field_as_str',
    'is_valid_email',
    'is_valid_password',
    'make_test_regex_fn',
    'MIN_DATE',
]

MIN_DATE = date.fromisoformat('1920-01-01')

def form_field_as_str(form_data: FormData, field_name: str) -> str:
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str')
#:

def form_field_as_file(form_data: FormData, field_name: str) -> UploadFile:
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is not UploadFile')
#:

def is_valid_name(name: str) -> bool:
    return all(len(parte) > 2 for parte in name.split())
#:

def is_valid_iso_date(iso_date: str) -> bool:
    try:
        date.fromisoformat(iso_date)
    except ValueError:
        return False
    else:
        return True
#:

def make_test_regex_fn(regex: str):
    compiled_regex = re.compile(regex)
    def test_regex_fn(value: str) -> bool:
        return bool(re.fullmatch(compiled_regex, value))
    return test_regex_fn
#:

is_valid_email = make_test_regex_fn(
    r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
)

is_valid_password = make_test_regex_fn(
    r"[0-9a-zA-Z\$\#\?\.\!]{3,10}"      # for testing purposes
)

def find_in(iterable: Iterable, predicate) -> Any | None:
    return next((obj for obj in iterable if predicate(obj)), None)
#:

# def find_in(iterable: Iterable, predicate) -> Any | None:
#     for obj in iterable:
#         if predicate(obj):
#             return obj
#     return None