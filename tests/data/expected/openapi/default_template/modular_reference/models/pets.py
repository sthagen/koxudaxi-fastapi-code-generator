# generated by fastapi-codegen:
#   filename:  modular_reference.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
