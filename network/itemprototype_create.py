from tools import asyncio,api,Base

hostid = Base['hostid']
ruleid = Base['network_discoveryrule_id']






async def loop_create():
    for data in item_prototypes:
        res = await api("itemprototype.create",data)
        print(res)

asyncio.run(loop_create())
