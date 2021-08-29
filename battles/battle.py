import json
from string import digits
from typethis import *

async def reconnectToBattle(msg, websocket):
    while msg[0:14] != "|updatesearch|":
        msg = await websocket.recv()
    await websocket.send("|/cancelsearch")
    msg = await websocket.recv()
    while msg[0:14] != "|updatesearch|":
        msg = await websocket.recv()
    games = json.loads(msg.replace("|updatesearch|", ""))['games']
    if games:
        for game in games:
            await websocket.send(f"|/join {game}")
            await choosemove(websocket, game)
    else:
        await search(websocket)

async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket):
    battleIDsearch = msg.find('battle-gen8metronomebattle')
    battleIDsearch2 = msg.find('\n')
    battleID = msg[battleIDsearch:battleIDsearch2]

    splitmsg = msg.splitlines()
    if '|upkeep' in splitmsg:
        splitmsg.remove('|upkeep')
    lastmsg = splitmsg[-1]
    remove_digits = str.maketrans('', '', digits)
    lastmsgWithoutDigits = lastmsg.translate(remove_digits)

    if msg == f'>{battleID}\n|request|':
        await timeron(websocket, battleID)
        await choosemove(websocket, battleID)

    if lastmsgWithoutDigits == '|turn|':
        await choosemove(websocket, battleID)

    if lastmsgWithoutDigits[0:5] == '|win|':
        await leave(websocket, battleID)
        await search(websocket)