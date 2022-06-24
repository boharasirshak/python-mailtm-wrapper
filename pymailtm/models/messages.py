from dataclasses import dataclass
from datetime import datetime
from pymailtm.models.common import (
    View, 
    Search
)

@dataclass
class From:
    name: str
    address: str


@dataclass
class To(From):
    pass


@dataclass
class Message:
    _id: str
    _type: str
    _context: str
    id: str
    account_id: str
    msg_id: str
    _from: From
    to: list[To]
    subject: str
    intro: str
    seen: bool
    is_deleted: bool
    has_attachments: bool
    size: int
    download_url: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Messages:
    member: list[Message]
    total_items: int
    view: View
    search: Search