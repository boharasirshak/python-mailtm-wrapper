import json
import requests
from datetime import datetime
from pymailtm import BASE_URL, SUCCESS_CODES
from pymailtm.models.accounts import Account
from pymailtm.models.errors import (
    CannotCreateAccountError,
    CannotGetAccountInfoError,
    UnauthorizedError
)

def create(address: str, password: str) -> Account:
    """Creates an Account resource 

    Args:
        address (str): The accounts address. Example user@example.com, The domain should be mail.tm's domain
        password (str): Account's password.

    Returns:
        Account: The account object
    """
    url = BASE_URL + '/accounts'
    body = {
        'address': address,
        'password': password
    }
    headers = {
        'accept': 'application/ld+json',
        'Content-Type': 'application/ld+json',
    }
    response = requests.post(
        url=url, 
        data=json.dumps(body), 
        headers=headers
    )
    if response.status_code not in SUCCESS_CODES:
        raise CannotCreateAccountError(
            message='Cannot create account', 
            status_code=response.status_code, 
            full_response=response.text
        )

    response = response.json()
    return Account(
        _context=response.get('@context'),
        _id=response.get('@id'),
        _type=response.get('@type'),
        id=response.get('id'),
        address=response.get('address'),
        quota=response.get('quota'),
        used=response.get('used'),
        is_disabled=response.get('isDisabled'),
        is_deleted=response.get('isDisabled'),
        created_at=datetime.strptime(response.get(
            'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
        updated_at=datetime.strptime(response.get(
            'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
    )


def get(id: str, token: str) -> Account:
    """Get an Account resource by its id

    Args:
        id (str): The account's id you want to get
        token (str): The account's auth Token

    Returns:
        Account: The account object
    """
    url = BASE_URL + f'/accounts/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code not in SUCCESS_CODES:
        if response.status_code == 401:
            raise UnauthorizedError(
                message='Invalid token',
                status_code=response.status_code,
                full_response=response.text
            )
        else:
            raise CannotGetAccountInfoError(
                message='Cannot get account info',
                status_code=response.status_code,
                full_response=response.text
            )
            
    response = response.json()
    return Account(
        _context=response.get('@context'),
        _id=response.get('@id'),
        _type=response.get('@type'),
        id=response.get('id'),
        address=response.get('address'),
        quota=response.get('quota'),
        used=response.get('used'),
        is_disabled=response.get('isDisabled'),
        is_deleted=response.get('isDisabled'),
        created_at=datetime.strptime(response.get(
            'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
        updated_at=datetime.strptime(response.get(
            'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
    )


def delete(id: str, token: str) -> bool:
    """Gets the account resource of the specified auth token

    Args:
        token (str): The account's auth Token

    Returns:
        bool: Returns True if success deleting account
    """
    url = BASE_URL + f'/accounts/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.delete(url, headers=headers)
    return response.status_code == 204


def me(token: str):
    """Get an Account resource by its id

    Args:
        id (str): The account's id you want to get
        token (str): The account's Bearer Token

    Returns:
        Account: The account object
    """
    url = BASE_URL + f'/me'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code not in SUCCESS_CODES:
        raise CannotGetAccountInfoError(
            message='Cannot get account info', 
            status_code=response.status_code, 
            full_response=response.text
        )

    response = response.json()
    return Account(
        _context=response.get('@context'),
        _id=response.get('@id'),
        _type=response.get('@type'),
        id=response.get('id'),
        address=response.get('address'),
        quota=response.get('quota'),
        used=response.get('used'),
        is_disabled=response.get('isDisabled'),
        is_deleted=response.get('isDisabled'),
        created_at=datetime.strptime(response.get(
            'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
        updated_at=datetime.strptime(response.get(
            'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
    )
