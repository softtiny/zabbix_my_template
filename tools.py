import aiohttp
import asyncio
import os
import json

ZABBIX_URL = os.environ['ZABBIX_URL']
ZABBIX_AUTH = os.environ['ZABBIX_AUTH']
with open("pi.json") as file:
    Base = json.load(file)
headers = {
        "Content-Type": "application/json",
        "Authorization": os.environ["ZABBIX_AUTH"],
        "Authorization": ZABBIX_AUTH,
        }

def json_fn(method:str,params):
    return {
            "jsonrpc": "2.0",
            "method":   method,
            "params": params,
            "id": 1,
    }

async def api(method:str,params):
    async with aiohttp.ClientSession() as session:
        async with session.post(ZABBIX_URL,json = json_fn(method,params),headers=headers) as res:
            return await res.json()




if __name__ == "__main__":
    import unittest
    class BaseTestCase(unittest.TestCase):
        def test_simple(self):
            print("run test simple")
            data = asyncio.run(api("item.get",{"output": "extend", "itemids": "42366",}))
            print(data)
    unittest.main()
