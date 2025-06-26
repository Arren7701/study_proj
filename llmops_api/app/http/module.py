# 所有外挂的模块都写在里面
from flask_migrate import Migrate
from injector import Module

from pkg.sqlalchemy import SQLAlchemy
from internal.extension import db, migrate


class ExtensionModule(Module):

    def configure(self,binder):
        binder.bind(SQLAlchemy,db)
        binder.bind(Migrate,migrate)
