from string import digits
from utils import login
from typethis import *

async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket):
    logConsSearch = msg.find('battle-gen8metronomebattle')
    logConsSearch2 = msg.find('\n')
    logCons = msg[logConsSearch:logConsSearch2]

    if msg == f'>{logCons}\n|request|':
        await timeron(websocket, logCons)
        await choosemove(websocket, logCons)
    splitws = msg.splitlines()

    if '|upkeep' in splitws != False:
        splitws.remove('|upkeep')
    lastmsg = splitws[-1]
    remove_digits = str.maketrans('', '', digits)
    lastmsgWithoutDigits = lastmsg.translate(remove_digits)

    if lastmsgWithoutDigits == '|turn|':
        await choosemove(websocket, logCons)

    if lastmsgWithoutDigits[0:5] == '|win|':
        await leave(websocket, logCons)
        await search(websocket)

    if login.Reconnected == True:
        await choosemove(websocket, logCons)
        login.Reconnected = False