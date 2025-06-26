import os

from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.model import App
from internal.router import Router, router
from pkg.response import HttpCode, json, Response
from pkg.sqlalchemy import SQLAlchemy


class Http(Flask):

    def __init__(self, *args,conf:Config,migrate:Migrate,db:SQLAlchemy,router:Router,**kwargs):


        # 初始化父类
        super().__init__(*args, **kwargs)

        # 配置的绑定   把自己创建的config绑定到flask上面，让flask自动配置
        self.config.from_object(conf)

        # 注册路由绑定
        router.register_router(self)

        # 异常注册处理
        self.register_error_handler(Exception,self._register_error_handler)


        # 建表
        db.init_app(self)

        with self.app_context():
            _=App()
            db.create_all()


        # 数据迁移初始化
        migrate.init_app(self,db,directory="internal/migration")



    def _register_error_handler(self,error:Exception):
        print("异常：", error)
        if isinstance(error,CustomException):
            return json(
                Response(code=error.code,message=error.message,data=error.data if error.data is not None else {}),
            )
        # if os.getenv("FLASK_ENV") == "development":
        #     raise error
        else:
            return json(Response(code=HttpCode.FAIL,message=str(error),data={}),)



