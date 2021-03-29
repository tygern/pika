import datetime
from dataclasses import dataclass


@dataclass
class BlogEntry():
    id: int
    title: str
    body: str
    author: str
    created_at: datetime
    updated_at: datetime
