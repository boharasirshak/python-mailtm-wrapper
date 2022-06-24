class MailTmError(Exception):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message)
        self._message = message
        self._status_code = status_code
        self._full_response = full_response
    
    @property
    def message(self) -> str:
        return self._message

    @property
    def status_code(self) -> int:
        return self._status_code
    
    @property
    def full_response(self) -> str:
        return self._full_response


class UnauthorizedError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotGetTokenError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotCreateAccountError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotGetAccountInfoError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotGetDomainError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotGetMessageError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotMarkMessageAsReadError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)
    

class CannotDeleteMessageError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)


class CannotGetSourceError(MailTmError):
    def __init__(self, message: str, status_code: int, full_response: str) -> None:
        super().__init__(message, status_code, full_response)