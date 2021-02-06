from string import digits
from utils import login
from utils.commands.typethis import *
from packteams import *
import random
import teams
import sys
battles = 0
async def search(websocket):
    team = random.choice(teams.teams)
    packed = PackTeam(team)
    await websocket.send(utm(team=packed))
    await websocket.send(laddersearch())
async def verifyBattle(msg, logCons, websocket):
    if msg == f'>{logCons}\n|request|':
        login.battleOn = True
        await websocket.send(timeron(logCons))
        await websocket.send(choosemove(logCons))
async def on_battle(msg, logCons, websocket):
    splitws = msg.splitlines()
    if '|upkeep' in splitws != False:
        splitws.remove('|upkeep')
    lastmsg = splitws[-1]
    remove_digits = str.maketrans('', '', digits)
    lastmsg = lastmsg.translate(remove_digits)
    if lastmsg == '|turn|':
        await websocket.send(choosemove(logCons))
    if lastmsg[0:5] == '|win|':
        await websocket.send(leave(logCons))
        global battles
        battles += 1
        print(battles)
        if battles == 80:
            sys.exit()
        else:
            await search(websocket=websocket)
