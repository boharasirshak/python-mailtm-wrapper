from dataclasses import dataclass
from datetime import datetime

@dataclass
class Account:
    _context: str
    _id: str
    _type: str
    id: str
    address: str
    quota: int
    used: int
    is_disabled: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime