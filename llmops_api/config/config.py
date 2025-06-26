import os
from typing import Any
from config.default_config import DEFAULT_CONFIG


def _get_env(key:str) -> Any:
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key:str) -> bool:
    value:str = _get_env(key)
    return  value.lower() == "true" if value is not None else False



class Config:
    def __init__(self):
        # 所有配置初始化

        # CSRF 保护机制
        # 测试环境：在单元测试中禁用 CSRF 可以简化测试流程，
        # 但建议使用专用的测试配置类（如 TestingConfig）。
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")
        self.SQLALCHEMY_DATABASE_URI = _get_env('SQLALCHEMY_DATABASE_URI')

        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size":_get_env( "SQLALCHEMY_POOL_SIZE"),
            "pool_recycle":_get_env("SQLALCHEMY_POOL_RECYCLE")
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")

