from dataclasses import dataclass
from datetime import datetime
from pymailtm.models.common import (
    View,
    Search
)


@dataclass
class Domain:
    _id: str
    _type: str
    _context: str
    id: str
    domain: str
    is_active: bool
    is_private: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class Domains():
    member: list[Domain]
    total_items: int
    view: View
    search: Search
