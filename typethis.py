import random
import teams
from packteams import *

def teamChoice():
    team = random.choice(teams.teams)
    packed = PackTeam(team)
    return packed

async def utm(websocket, team):
    return await websocket.send(f'|/utm {team}')

async def laddersearch(websocket):
    return await websocket.send('|/search gen8metronomebattle')

async def challenge(websocket, user):
    return await websocket.send(f'|/challenge {user}, gen8metronomebattle')

async def choosemove(websocket, battleID):
    return await websocket.send(f'{battleID}|/choose default')

async def timeron(websocket, battleID):
    return await websocket.send(f'{battleID}|/timer on')

async def leave(websocket, battleID):
    return await websocket.send(f'/noreply |/leave {battleID}')