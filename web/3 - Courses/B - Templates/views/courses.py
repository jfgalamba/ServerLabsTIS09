from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get('/courses')
async def courses():
    return {}
#:

