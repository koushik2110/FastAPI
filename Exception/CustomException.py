
class OwnException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class NotFoundException(OwnException):
    def __init__(self, error_message: str):
        super().__init__(error_message+" Not Found", 404)


class ValidationFailed(OwnException):
    def __init__(self, error_message: str):
        super().__init__(" Validation Failed: "+error_message, 400)