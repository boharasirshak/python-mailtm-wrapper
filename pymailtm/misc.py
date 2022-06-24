import json
import requests
from pymailtm.models import Token
from pymailtm import BASE_URL, SUCCESS_CODES
from pymailtm.models.errors import CannotGetTokenError


def get_token(address: str, password: str):
    """Gets the accounts bearer token

    Args:
        address (str): The Accounts address. Example user@example.com, The domain should be mail.tm's domain
        password (str): Account's password.

    Raises:
        CannotGetTokenError: When the username or password doesn't match the account

    Returns:
        Account: The account object
    """
    url = BASE_URL + '/token'
    body = {
        'address': address,
        'password': password
    }
    headers = {
        'content-type': 'application/ld+json',
    }
    response = requests.post(
        url=url, 
        data=json.dumps(body), 
        headers=headers
    )
    if response.status_code not in SUCCESS_CODES:
        raise CannotGetTokenError(
                message='Cannot get token',
                status_code=response.status_code,
                full_response=response.text
            )
    
    response = response.json()
    return Token(
        id=response.get('id'),
        token=response.get('token')
    )