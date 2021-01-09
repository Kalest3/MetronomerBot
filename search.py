from login import *
def laddersearch():
    return '|/search gen8metronomebattle'
def challenge(user):
    return f'|/challenge {user}, gen8metronomebattle'
def utm(team):
    return f'|/utm {team}'
async def search():
    import awaitbattle
    teams = []
    teamstxt = open('teams.txt', 'r')
    read = teamstxt.readlines()
    for ler in read:
        teams.append(ler.strip())
    choice = random.choice(teams)
    await websocket.send(utm(team=choice))
    await websocket.send(laddersearch())
    await awaitbattle.awaitar()