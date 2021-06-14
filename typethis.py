import showdown
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
async def accept(websocket, user):
    return await websocket.send(f'|/accept {showdown.utils.name_to_id(user)}')
async def choosemove(websocket, logCons):
    return await websocket.send(f'{logCons}|/choose default')
async def timeron(websocket, logCons):
    return await websocket.send(f'{logCons}|/timer on')
async def leave(websocket, logCons):
    return await websocket.send(f'/noreply |/leave {logCons}')