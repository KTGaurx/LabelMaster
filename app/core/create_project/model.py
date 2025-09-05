from typing import Any, Dict, List

from pydantic import BaseModel


def req_create_project(BaseModel):
    name: str
    description: str
    framwork: str
    task: str


def res_create_project(BaseModel):
    project_id: int
    name: str
    description: str
    framwork: str
    task: str
