from string import digits
from typethis import *
from utils import login

async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket):
    battleIDsearch = msg.find('battle-gen8metronomebattle')
    battleIDsearch2 = msg.find('\n')
    battleID = msg[battleIDsearch:battleIDsearch2]

    splitws = msg.splitlines()
    if '|upkeep' in splitws:
        splitws.remove('|upkeep')
    lastmsg = splitws[-1]
    remove_digits = str.maketrans('', '', digits)
    lastmsgWithoutDigits = lastmsg.translate(remove_digits)

    if msg == f'>{battleID}\n|request|':
        await timeron(websocket, battleID)
        await choosemove(websocket, battleID)

    if login.Reconnected:
        await choosemove(websocket, battleID)
        login.Reconnected = False

    if lastmsgWithoutDigits == '|turn|':
        await choosemove(websocket, battleID)

    if lastmsgWithoutDigits[0:5] == '|win|':
        await leave(websocket, battleID)
        await search(websocket)