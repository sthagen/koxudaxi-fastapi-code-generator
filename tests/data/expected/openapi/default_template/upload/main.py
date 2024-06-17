# generated by fastapi-codegen:
#   filename:  upload.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import Optional, Union

from fastapi import FastAPI, Request, UploadFile

from .models import Error

app = FastAPI(
    version='1.0.0',
    title='Swagger Petstore',
    license={'name': 'MIT'},
    description='API definiton for testing file upload',
    servers=[{'url': 'http://petstore.swagger.io/v1'}],
)


@app.post(
    '/pets/{id}/image/form-data',
    response_model=None,
    responses={'default': {'model': Error}},
    tags=['pets'],
)
def upload_pet_image_with_form_data(id: str, file: UploadFile = ...) -> Optional[Error]:
    """
    Upload image with Form-Data for a pet
    """
    pass


@app.post(
    '/pets/{id}/image/octet-stream',
    response_model=None,
    responses={'default': {'model': Error}},
    tags=['pets'],
)
def upload_pet_image_with_octet_stream(
    id: str, request: Request = ...
) -> Optional[Error]:
    """
    Upload image with octet-stream for a pet
    """
    pass