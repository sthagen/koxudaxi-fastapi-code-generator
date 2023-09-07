# generated by fastapi-codegen:
#   filename:  body_and_parameters.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI, Path, Query, Request
from starlette.requests import Request

from .models import (
    Error,
    Pet,
    PetForm,
    UserGetResponse,
    UserPostRequest,
    UsersGetResponse,
    UsersPostRequest,
)

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description='This description is for testing\nmulti-line\ndescription\n',
    servers=[{'url': 'http://petstore.swagger.io/v1'}],
)


@app.post('/bar', response_model=None, tags=['bar'])
def post_bar(request: Request) -> None:
    """
    Create a bar
    """
    pass


@app.post('/convert', response_model=bytes)
def convert1(format: Optional[str] = 'pdf', request: Request = ...) -> bytes:
    pass


@app.put('/convert', response_model=bytes)
def convert2(format: Optional[str] = None, request: Request = ...) -> bytes:
    pass


@app.get('/foo', response_model=str, tags=['foo'])
def get_foo(foo: Optional[str] = None) -> str:
    pass


@app.post(
    '/food', response_model=None, responses={'default': {'model': str}}, tags=['pets']
)
def post_food(body: str) -> Union[None, str]:
    """
    Create a food
    """
    pass


@app.get('/food/{food_id}', response_model=List[int], tags=['foods'])
def show_food_by_id(
    food_id: str, message_texts: Optional[List[str]] = None
) -> List[int]:
    """
    Info for a specific pet
    """
    pass


@app.get(
    '/pets',
    response_model=List[Pet],
    responses={'default': {'model': Error}},
    tags=['pets'],
)
def list_pets(
    limit: Optional[int] = 0,
    home_address: Optional[str] = Query('Unknown', alias='HomeAddress'),
    kind: Optional[str] = 'dog',
) -> Union[List[Pet], Error]:
    """
    List all pets
    """
    pass


@app.post(
    '/pets', response_model=None, responses={'default': {'model': Error}}, tags=['pets']
)
def post_pets(body: PetForm) -> Union[None, Error]:
    """
    Create a pet
    """
    pass


@app.get(
    '/pets/{petId}',
    response_model=Pet,
    responses={'default': {'model': Error}},
    tags=['pets'],
)
def show_pet_by_id(pet_id: str = Path(..., alias='petId')) -> Union[Pet, Error]:
    """
    Info for a specific pet
    """
    pass


@app.put(
    '/pets/{petId}',
    response_model=None,
    responses={'default': {'model': Error}},
    tags=['pets'],
)
def put_pets_pet_id(
    pet_id: str = Path(..., alias='petId'), body: PetForm = None
) -> Union[None, Error]:
    """
    update a pet
    """
    pass


@app.get('/user', response_model=UserGetResponse, tags=['user'])
def get_user() -> UserGetResponse:
    pass


@app.post('/user', response_model=None, tags=['user'])
def post_user(body: UserPostRequest) -> None:
    pass


@app.get('/users', response_model=List[UsersGetResponse], tags=['user'])
def get_users() -> List[UsersGetResponse]:
    pass


@app.post('/users', response_model=None, tags=['user'])
def post_users(body: List[UsersPostRequest]) -> None:
    pass


@app.post(
    '/{ueId}/sdm-subscriptions', response_model=None, tags=['Subscription Creation']
)
def subscribe(ue_id: str = Path(..., alias='ueId'), body: Pet = ...) -> None:
    """
    subscribe to notifications
    """
    pass
