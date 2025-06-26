## 埋点，通过埋点分析用户的行为。
## 埋点分两种，一个是业务埋点，业务非常关心；一个是异常埋点，质量非常关心
## 通过exception监测。
from dataclasses import field
from importlib.metadata import pass_none
from typing import Any

from pkg.response import HttpCode, message


class CustomException(Exception):
    code:HttpCode = HttpCode.FAIL
    message:str = ""
    data:Any = field(default=dict)

    def __init__(self,message:str,data:Any=None):
        super().__init__(message())
        self.message = message()
        self.data = data



# 失败的
class FailedException(CustomException):
    pass

# not found
class NotFoundException(CustomException):
    code:HttpCode = HttpCode.NOT_FOUND

class UnauthorizedException(CustomException):
    code:HttpCode = HttpCode.UNAUTHORIZED

class ValidationException(CustomException):
    code:HttpCode = HttpCode.VALIDATE_ERROR

class ForbiddenException(CustomException):
    code:HttpCode = HttpCode.FORBIDDEN



# 未授权的异常



# 未发现的exception




# forbidden 异常








