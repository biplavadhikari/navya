from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomResponse(Response):
    def __init__(self, data=None, message="", success=True, status=200, headers=None, **kwargs):
        super().__init__(headers=headers, status=status)
        self.data = {"data": data, "message": message, "success": success, **kwargs}


class CustomException(APIException):
    def __init__(self, data=None, message="", success=False, status=400, **kwargs):
        super().__init__()
        self.detail = {"data": data, "message": message, "success": success, **kwargs}
        self.status_code = status

    def __str__(self):
        return self.detail["message"]
