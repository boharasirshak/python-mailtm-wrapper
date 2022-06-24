import requests
from datetime import datetime
from pymailtm import BASE_URL, SUCCESS_CODES
from pymailtm.models.common import (
    View,
    Search,
    Mapping
)
from pymailtm.models.domains import (
    Domains,
    Domain
)
from pymailtm.models.errors import (
    UnauthorizedError,
    CannotGetDomainError
)


def get(page: int = 1) -> Domains:
    """Returns a list of domains

    Args:
        page (int, optional): The collection page number. Defaults to 1.

    Returns:
        Domains: The domain object containing result
    """
    url = BASE_URL + '/domains'
    params = {
        'page': page
    }
    response = requests.get(url=url, params=params)
    if response.status_code not in SUCCESS_CODES:
        raise CannotGetDomainError(
            message='Cannot get domain info',
            status_code=response.status_code,
            full_response=response.text
        )
    response = response.json()
    domains: list[Domain] = []

    for member in response.get('hydra:member', []):
        domain = Domain(
            _id=member.get('@id'),
            _type=member.get('@type'),
            _context=member.get('@context'),
            id=member.get('id'),
            domain=member.get('domain'),
            is_active=member.get('isActive'),
            is_private=member.get('isPrivate'),
            created_at=datetime.strptime(member.get(
                'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
            updated_at=datetime.strptime(member.get(
                'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
        )
        domains.append(domain)

    total_items = response.get('hydra:totalItems')
    view = View(
        _id=response.get('hydra:view', {}).get('@id'),
        _type=response.get('hydra:view', {}).get('@type'),
        first=response.get('hydra:view', {}).get('hydra:first'),
        last=response.get('hydra:view', {}).get('hydra:last'),
        previous=response.get('hydra:view', {}).get('hydra:previous'),
        next=response.get('hydra:view', {}).get('hydra:next'),
    )
    mapping = Mapping(
        _type=response.get('hydra:search', {}).get(
            'hydra:mapping', {}).get('@type'),
        variable=response.get('hydra:search', {}).get(
            'hydra:mapping', {}).get('variable'),
        property=response.get('hydra:search', {}).get(
            'hydra:mapping', {}).get('property'),
        required=response.get('hydra:search', {}).get(
            'hydra:mapping', {}).get('required'),
    )
    search = Search(
        _type=response.get('hydra:search', {}).get('@type'),
        template=response.get('hydra:search', {}).get('hydra:template'),
        variable_representation=response.get(
            'hydra:search', {}).get('hydra:variableRepresentation'),
        mapping=mapping,
    )
    return Domains(
        member=domains,
        total_items=total_items,
        view=view,
        search=search
    )


def get_by_id(id: str, token: str) -> Domain:
    """Retreives a domain by its id

    Args:
        id (str): The domain you want to get with id
        token (str): The auth token

    Returns:
        Domains: The domain object containing result
    """
    url = BASE_URL + f'/domains/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code not in SUCCESS_CODES:
        if response.status_code == 401:
            raise UnauthorizedError(
                message='Invalid token',
                status_code=response.status_code,
                full_response=response.text
            )
        else:
            raise CannotGetDomainError(
                message='Cannot get domain info',
                status_code=response.status_code,
                full_response=response.text
            )

    response = response.json()
    return Domain(
        _id=response.get('@id'),
        _type=response.get('@type'),
        _context=response.get('@context'),
        id=response.get('id'),
        domain=response.get('domain'),
        is_active=response.get('isActive'),
        is_private=response.get('isPrivate'),
        created_at=datetime.strptime(response.get(
            'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
        updated_at=datetime.strptime(response.get(
            'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
    )
