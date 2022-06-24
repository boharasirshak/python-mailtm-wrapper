import requests
from pymailtm import BASE_URL, SUCCESS_CODES
from pymailtm.models.sources import Source
from pymailtm.models.errors import (
    UnauthorizedError,
    CannotGetSourceError
)


def get(id: str, token: str):
    """Gets a Message's source

    Args:
        id (str): The id of the source
        token (str): The user bearer token

    Raises:
        UnauthorizedError: When the token is invalid or doesn't correspond to the id
        CannotGetSourceError: When the id is invalid

    Returns:
        Source: The source
    """
    url = BASE_URL + f'/sources/{id}'
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
            raise CannotGetSourceError(
                message='Cannot get the source',
                status_code=response.status_code,
                full_response=response.text
            )
    
    response = response.json()
    return Source (
        _id=response.get('@id'),
        _type=response.get('@type'),
        _context=response.get('@context'),
        id=response.get('id'),
        download_url=response.get('downloadUrl'),
        data=response.get('data'),
    )
