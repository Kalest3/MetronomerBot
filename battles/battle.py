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
    else:
        await search(websocket)

async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket):
    newTurn = False
    battleEnd = False
    battleIDsearch = msg.find('battle-gen8metronomebattle')
    battleIDsearch2 = msg.find('\n')
    battleID = msg[battleIDsearch:battleIDsearch2]

    if msg == f'>{battleID}\n|request|':
        await timeron(websocket, battleID)
        await choosemove(websocket, battleID)

    splitmsg = msg.splitlines()
    for line in splitmsg:
        if line[0:6] == "|turn|":
            newTurn = True
        if line[0:5] == "|win|":
            battleEnd = True
    if newTurn: 
        await choosemove(websocket, battleID)
    if battleEnd: 
        await leave(websocket, battleID) 
        await search(websocket)