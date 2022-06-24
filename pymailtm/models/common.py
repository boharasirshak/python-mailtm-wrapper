from dataclasses import dataclass

@dataclass
class View:
    _id: str
    _type: str
    first: str
    last: str
    previous: str
    next: str


@dataclass
class Mapping:
    _type: str
    variable: str
    property: str
    required: bool


@dataclass
class Search:
    _type: str
    template: str
    variable_representation: str
    mapping: Mapping
