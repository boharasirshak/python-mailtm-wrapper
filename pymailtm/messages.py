import requests
from datetime import datetime
from pymailtm import BASE_URL, SUCCESS_CODES
from pymailtm.models.common import (
    View,
    Search,
    Mapping
)
from pymailtm.models.messages import (
    To,
    From,
    Message,
    Messages
)
from pymailtm.models.errors import (
    CannotGetMessageError,
    UnauthorizedError,
    CannotMarkMessageAsReadError,
    CannotDeleteMessageError
)


def getall(page: int, token: str):
    """Gets all Messages corresponsing to the user's token

    Args:
        page (int): The page number
        token (str): The user bearer token

    Raises:
        UnauthorizedError: When the token is invalid
        CannotGetMessageError: When the page is invalid

    Returns:
        Messages: The messages
    """
    url = BASE_URL + '/messages'
    params = {
        'page': page,
    }
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.get(
        url=url,
        params=params,
        headers=headers
    )

    if response.status_code not in SUCCESS_CODES:
        if response.status_code == 401:
            raise UnauthorizedError(
                message='Invalid token',
                status_code=response.status_code,
                full_response=response.text
            )
        else:
            raise CannotGetMessageError(
                message='Cannot get message',
                status_code=response.status_code,
                full_response=response.text
            )

    response = response.json()
    messages: list[Message] = []

    for member in response.get('hydra:member', []):
        to_s: list[To] = []
        _from = From(
            name=member.get('name'),
            address=member.get('address')
        )
        for _to in member.get('to', []):
            to_s.append(To(
                name=_to.get('name'),
                address=_to.get('address')
            ))
        message = Message(
            _id=member.get('@id'),
            _type=member.get('@type'),
            _context=member.get('@context'),
            id=member.get('id'),
            account_id=member.get('accountId'),
            msg_id=member.get('msgid'),
            to=to_s,
            _from=_from,
            subject=member.get('subject'),
            intro=member.get('intro'),
            seen=member.get('seen'),
            is_deleted=member.get('isDeleted'),
            has_attachments=member.get('hasAttachments'),
            size=member.get('size'),
            download_url=member.get('downloadUrl'),
            created_at=datetime.strptime(member.get(
                'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
            updated_at=datetime.strptime(member.get(
                'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
        )
        messages.append(message)

    total_items = response.get('hydra:totalItems', 0)
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
    return Messages(
        member=messages,
        total_items=total_items,
        view=view,
        search=search
    )


def get(id: str, token: str):
    """_summary_: Gets a Message's Source resource

    Args:
        id (str): The id of the source
        token (str): The user bearer token

    Raises:
        UnauthorizedError: When the token is invalid or doesn't corresponds to the id
        CannotGetMessageError: When the id is invalid

    Returns:
        Message: The message
    """
    url = BASE_URL + f'/messages/{id}'
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
            raise CannotGetMessageError(
                message='Cannot get message',
                status_code=response.status_code,
                full_response=response.text
            )

    response = response.json()
    to_s: list[To] = []
    _from = From(
        name=response.get('name'),
        address=response.get('address')
    )
    for _to in response.get('to', []):
        to_s.append(To(
            name=_to.get('name'),
            address=_to.get('address')
        ))
    return Message(
        _id=response.get('@id'),
        _type=response.get('@type'),
        _context=response.get('@context'),
        id=response.get('id'),
        account_id=response.get('accountId'),
        msg_id=response.get('msgid'),
        to=to_s,
        _from=_from,
        subject=response.get('subject'),
        intro=response.get('intro'),
        seen=response.get('seen'),
        is_deleted=response.get('isDeleted'),
        has_attachments=response.get('hasAttachments'),
        size=response.get('size'),
        download_url=response.get('downloadUrl'),
        created_at=datetime.strptime(response.get(
            'createdAt'), '%Y-%m-%dT%H:%M:%S+00:00'),
        updated_at=datetime.strptime(response.get(
            'updatedAt'), '%Y-%m-%dT%H:%M:%S+00:00')
    )


def delete(id: str, token: str):
    """Deletes a Message's Source resource

    Args:
        id (str): The id of the source
        token (str): The user bearer token

    Raises:
        UnauthorizedError: When the token is invalid or doesn't corresponds to the id
        CannotDeleteMessageError: When the id is invalid

    Returns:
        _type_: True if successful, False otherwise
    """
    url = BASE_URL + f'/messages/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.delete(url=url, headers=headers)
    if response.status_code not in SUCCESS_CODES:
        if response.status_code == 401:
            raise UnauthorizedError(
                message='Invalid token',
                status_code=response.status_code,
                full_response=response.text
            )
        else:
            raise CannotDeleteMessageError(
                message='Cannot delete the message',
                status_code=response.status_code,
                full_response=response.text
            )

    return response.status_code == 204


def mark_as_read(id: str, token: str):
    """Marks a Message as read

    Args:
        id (str): The id of the source
        token (str): The user bearer token

    Raises:
        UnauthorizedError: When the token is invalid or doesn't corresponds to the id
        CannotMarkMessageAsReadError: When the id is invalid

    Returns:
        bool: True if the message is seen othwewise false
    """
    url = BASE_URL + f'/messages/{id}'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/ld+json',
    }
    response = requests.patch(url=url, headers=headers)

    if response.status_code not in SUCCESS_CODES:
        if response.status_code == 401:
            raise UnauthorizedError(
                message='Invalid token',
                status_code=response.status_code,
                full_response=response.text
            )
        else:
            raise CannotMarkMessageAsReadError(
                message='Cannot mark as read',
                status_code=response.status_code,
                full_response=response.text
            )

    return response.json().get('seen', False)
