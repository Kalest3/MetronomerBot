import random
import teams
from packteams import *

def teamChoice():
    """Choice a team in teams.py
    """
    team = random.choice(teams.teams)
    packed = PackTeam(team)
    return packed

async def utm(websocket, team):
    """Uses a specified team to battle.
    """
    return await websocket.send(f'|/utm {team}')

async def laddersearch(websocket):
    """Search a battle in ladder.
    """
    return await websocket.send('|/search gen8metronomebattle')

async def challenge(websocket, user):
    """Challenges a user.
    """
    return await websocket.send(f'|/challenge {user}, gen8metronomebattle')

async def choosemove(websocket, battleID):
    """Chooses the only move choiceable on a Metronome Battle.
    """
    return await websocket.send(f'{battleID}|/choose default')

async def timeron(websocket, battleID):
    """Start the timer on a Metronome Battle.
    """
    return await websocket.send(f'{battleID}|/timer on')

async def leave(websocket, battleID):
    """Leaves from a battle.
    """
    return await websocket.send(f'/noreply |/leave {battleID}')