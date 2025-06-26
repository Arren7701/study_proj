import uuid

from injector import inject
from dataclasses import dataclass


from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class Appservice:
    db : SQLAlchemy
    def create_app(self)->App:
        with self.db.auto_commit():
            app = App(name="测试ai机器人",
                      account_id = uuid.uuid4(),
                      icon="",
                      description="这是一个测试机器人")
        # 增加一个app的数据
            self.db.session.add(app)
        return app

    def get_app(self,id:uuid.UUID)->App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self,id:uuid.UUID)->App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "arren的第一个机器人"
        return app

    def delete_app(self,id:uuid.UUID)->App:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app







