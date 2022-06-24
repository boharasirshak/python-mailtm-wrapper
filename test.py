from pymailtm import accounts
from pymailtm import domains
from pymailtm import sources
from pymailtm import messages
from pymailtm import get_token
from pymailtm.utils import generate_password

results = domains.get()

domain = results.member[0].domain
print(domain)

username = f'yourusernamehere@{domain}'
password = generate_password()

print(f'{username=} has {password=}')

try:
    account = accounts.create(username, password)

except Exception as e:
    print(e.message)
    print(e.status_code)
    print(e.full_response)
    exit()

token = get_token(username, password).token

msgs = messages.getall(page=1, token=token)
if msgs.total_items == 0:
    print('No messages')
else:
    msg_id = msgs.member[0].id
    print(f'Message id {msg_id}')
    msg = messages.get(msg_id, token)
