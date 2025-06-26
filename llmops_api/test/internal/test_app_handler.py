import pytest
import requests

from pkg.response import HttpCode


class TestHandler:
    def test_ping(self,client):
        r = client.get("/ping")
        print("r\n Recive Data:",r.json)
        assert r.status_code == 200
        assert r.json.get("ping") == "pong"


    @pytest.mark.parametrize("query", [None,"你好，你是谁？"])
    def test_completion(self,query,client):
        r = client.post("/apps/completion",json = {"query":query})
        print(r.json)
        assert r.status_code == 200\

        if query is None:
            assert r.json.get("code")==HttpCode.VALIDATE_ERROR
        else:
            assert r.json.get("code")==HttpCode.SUCCESS

    @pytest.mark.parametrize("query", [None,"你是谁？"])
    def test_completion_with_request(self,query):
        url = "http://127.0.0.1:5000/apps/completion"
        headers = {"Content-Type":"application/json"}
        resp = requests.post(url,headers=headers,json={"query":query})
        print(resp.json())
        assert resp.status_code == 200






    #
    #
    # def test_completion2(self,client):
    #     r = client.post("/apps/completion",json = {"query":"你是谁?"})
    #     assert r.status_code == 200
    #     assert r.json.get("code") == "success"
    #     print(r.json)
