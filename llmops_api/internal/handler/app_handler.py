import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject, Injector
from openai import OpenAI


from internal.schema import CompletionReq
from internal.service.app_service import Appservice
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    app_service: Appservice
    # 把appservice注入到apphandler里面，让里面的函数可以运行起来。

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为 {app.id}")

    def get_app(self,id:uuid.UUID):
        app = self.app_service.create_app()
        return success_message(f"应用的名字是{app.name}")

    def update_app(self,id:uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改后的名字是{app.name}")

    def delete_app(self,id:uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，删除id为：{app.id}")

    def ping(self):
        return {"ping": "pong"}

    def completion(self):
        req = CompletionReq()

        if not req.validate():
            return validate_error_json(req.errors)

        query = request.json.get("query")

        client = OpenAI() #可以不写内容，只要env的配置和默认保持一致

        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo-16k",
            messages = [
                {"role":"system","content":"你是OpenAI的机器人，请根据用户的问题来回答"},
                {"role":"user","content":query},
            ])

        ai_rsp = completion.choices[0].message.content
        print(completion.choices)
        return success_json({"content":ai_rsp})

