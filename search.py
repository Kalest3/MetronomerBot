from login import *
async def search():
    import awaitbattle
    teams = []
    teamstxt = open('teams.txt', 'r')
    read = teamstxt.readlines()
    for ler in read:
        teams.append(ler.strip())
    choice = random.choice(teams)
    await websocket.send(f'|/utm {choice}')
    await websocket.send('|/search gen8metronomebattle')
    await awaitbattle.awaitar()