from login import *
def laddersearch():
    return '|/search gen8metronomebattle'
def challenge(user):
    return f'|/challenge {user}, gen8metronomebattle'
def utm(team):
    return f'|/utm {team}'
async def search():
    import awaitbattle
    await websocket.send(utm(team=choice))
    await websocket.send(laddersearch())
    await awaitbattle.awaitar()