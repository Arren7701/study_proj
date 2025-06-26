from dataclasses import dataclass
from typing import Any

from attrs import field
from flask import jsonify

from pkg.response import HttpCode

@dataclass
class Response():
    code:HttpCode = HttpCode.SUCCESS
    message:str = ""
    data:Any = field(default=dict)


# 返回json数据格式的函数定义
def json(data:Response=None):
    return jsonify(data),200

# 返回成功的json
def success_json(data:Any=None):
    return json(Response(code=HttpCode.SUCCESS,message="",data=data))

# 返回失败的json
def fali_json(data:Any=None):
    return json(Response(code=HttpCode.FAIL,message="",data=data))

# 返回Validate error json
def validate_error_json(errors:dict):
    first_key = next(iter(errors))

    if first_key is not None:
        ret_msg = errors.get(first_key)
        return json(Response(code=HttpCode.VALIDATE_ERROR,message=ret_msg,data=errors))
    else:
        return json(Response(code=HttpCode.VALIDATE_ERROR,message="",data=errors))


# 返回 message 接口设计
def message(code:HttpCode=None,msg:str=""):
    return json(Response(code = code,message = msg,data = {}))

# 成功的msg
def success_message(msg:str=""):
    return message(HttpCode.SUCCESS,msg = msg)

# 失败的message
def fali_message(msg:str=""):
    return message(HttpCode.FAIL,msg = msg)

# 没有发现的msg
def not_found_message(msg:str=""):
    return message(HttpCode.NOT_FOUND,msg = msg)


# 没有授权的msg
def unauthorized_message(msg:str=""):
    return message(HttpCode.UNAUTHORIZED,msg = msg)


# 禁止访问
def forbidden_message(msg:str=""):
    return message(HttpCode.FORBIDDEN,msg = msg)





