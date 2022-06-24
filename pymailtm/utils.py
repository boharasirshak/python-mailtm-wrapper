import string
import random

CHARS = string.ascii_letters + string.digits

def generate_password(length: int = 10):
    """Generates a random password of given length 

    Args:
        length (int, optional): The length of password. Defaults to 10.

    Returns:
        str: The random generated password
    """
    chatset = [random.choice(CHARS) for _ in range(length)]
    return ''.join(chatset)