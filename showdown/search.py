from showdown.login import *
from packteams import *
def laddersearch():
    return '|/search gen8metronomebattle'
def challenge(user:str):
    return f'|/challenge {user}, gen8metronomebattle'
def utm(team):
    return f'|/utm {team}'
async def search():
    from battles import awaitbattle
    await websocket.send(utm(team=packed))
    await websocket.send(laddersearch())
    await awaitbattle.awaitar()