from flask import Flask, Blueprint
from injector import inject
from dataclasses import dataclass

from sqlalchemy.util import methods_equivalent

from internal.handler import app_handler
from internal.handler.app_handler import AppHandler


@inject #标记 构造函数class Router 需要依赖注入
@dataclass #告诉框架 我不需要init函数
class Router:
    app_handler: AppHandler

    def register_router(self, app:Flask):
        blue_printer = Blueprint('llmops-api-server', __name__, url_prefix = "")
        blue_printer.add_url_rule("/ping",methods = ["get"],view_func=self.app_handler.ping)
        blue_printer.add_url_rule("/apps/completion",methods = ["post"],view_func = self.app_handler.completion)

        blue_printer.add_url_rule("/app",methods = ["POST"],view_func=self.app_handler.create_app)
        blue_printer.add_url_rule("/app/<uuid:id>",view_func=self.app_handler.get_app)
        blue_printer.add_url_rule("/app/<uuid:id>",methods = ["POST"],view_func=self.app_handler.update_app)
        blue_printer.add_url_rule("/app/<uuid:id>/delete",methods = ["POST"],view_func=self.app_handler.delete_app)



        app.register_blueprint(blue_printer)
    pass



'''
Blueprint（蓝图） 是一种组织大型应用的方式，
它可以将路由、模板、静态文件等组件按功能模块拆分，让代码结构更清晰.
小型应用：可以把所有路由写在一个文件里,但是大型的应用，如果有数十个路由，代码会变得难以维护。
蓝图可以将代码按功能拆分（例如用户管理、文章管理、API 等）
'''

