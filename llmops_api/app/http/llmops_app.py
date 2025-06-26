import dotenv
from flask_migrate import Migrate

from injector import Injector

from app.http.module import ExtensionModule
from internal.router import Router
from internal.server import Http
from config import Config
from pkg.sqlalchemy import SQLAlchemy

## 导入全局的配置
dotenv.load_dotenv()



## 构建了一个注入器
app_injector = Injector([ExtensionModule])

"""
依赖注入的核心思想是：对象的依赖由外部提供，而不是在对象内部创建。
对扩展开放，对修改关闭
Injector 类的作用:
    自动创建对象：根据类型信息自动创建和注入依赖。
    管理单例：确保某个类在整个应用中只有一个实例。
    解耦组件：让代码不需要硬编码依赖关系。

app_injector = Injector() 创建了一个依赖注入容器，用于：
    自动管理对象的创建和依赖关系。
    让代码更灵活、可测试和可维护。
    避免硬编码依赖，遵循依赖倒置原则。
"""


# 从config导入并构建CSRF 保护机制
app_config=Config()


## 新建一个flask http 服务
run_app = Http(__name__,
               conf = app_config, # 项目的配置
               db =  app_injector.get(SQLAlchemy), # 项目的数据库
               migrate=app_injector.get(Migrate), # 数据库的迁移
               router = app_injector.get(Router) # 项目路由
               )

## 通过注入的方式给http构建一个router

if __name__ == '__main__':
    run_app.run()


