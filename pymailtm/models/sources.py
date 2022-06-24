from dataclasses import dataclass

@dataclass
class Source:
    _id: str
    _type: str
    _context: str
    id: str
    download_url: str
    data: str
