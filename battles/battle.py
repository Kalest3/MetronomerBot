from string import digits
from utils import login
from utils.commands.typethis import *
from packteams import *
import random
import teams
battles = 0
async def search(websocket):
    team = random.choice(teams.teams)
    packed = PackTeam(team)
    await websocket.send(utm(team=packed))
    await websocket.send(challenge('gabrielgottapok'))
async def verifyBattle(msg, logCons, websocket):
    if msg == f'>{logCons}\n|request|':
        await websocket.send(timeron(logCons))
        await websocket.send(choosemove(logCons))
        login.battleOn = True
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
        login.battleOn = False
        global battles
        battles += 1
        print(battles)
        await search(websocket=websocket)
    if login.Reconnected == True:
        await websocket.send(choosemove(logCons))
        login.Reconnected = False