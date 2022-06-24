# Unofficial Python mail.tm API Wrapper

This is an unofficial wrapper for [mail.tm](https://mail.tm) API. <br>
Since the official python wrapper of **mail.tm** focuses more on real life uses cases of **mail.tm** and less on wrapping the API, I found it uncomfortable to work with it in my personal project, so I decided to make this API wrapper and make it open source for public use.

#

## Basic Usage 

### Installation
_Sorry, but this api is not currently published on pypi_

#

### Dependencies
`pip install requests`

#


### Creating an new account


```python
from pymailtm import accounts
from pymailtm import domains
from pymailtm import get_token
from pymailtm.models.errors import MailTmError

domains_list = domains.get()
domain = results.member[0].domain

username = f'your_username@{domain}'
password = 'YourPassword'

try:
    account = accounts.create(username, password)
    print(f'Accounts id is {account.id}')

except MailTmError as e:
    print(e.message)
    print(e.full_response)

```


#

### Getting account token


```python
from pymailtm import get_token

username = f'your_username@domain.com'
password = 'YourPassword'

try:
    token = get_token(username, password).token
    print(f'Accounts token is {token}')

except MailTmError as e:
    print(e.message)
    print(e.full_response)

```

#

### Getting account messages

```python
from pymailtm import messages
from pymailtm import get_token

token = 'mailtm_account_token'

try:
    msgs = messages.getall(page=1, token=token)

    if msgs.total_items == 0:
        print('No messages found')
        exit()

    msg_id = msgs.member[0].id
    print(f'Message id {msg_id}')

except MailTmError as e:
    print(e.message)
    print(e.full_response)

```

#

Please refer to the [mail.tm official api](https://docs.mail.tm/) for more information and resources

#

## Todo

- [ ] Making the Errors more discriptive and meaningful
- [ ] Removing duplicate codes
- [ ] Adding more utility methods and helpers
