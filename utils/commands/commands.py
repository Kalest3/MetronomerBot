from config import username
from run import *

def PM(userSearch, command: str):
   return f'|pm|{userSearch}|{username}|@{command}'
async def spheal(websocket, user: str):
   return await websocket.send(f'|/pm {user}, spheal')
async def commands(websocket, user: str):
   return await websocket.send(f'|/pm {user}, See my commands at: https://github.com/Kalest3/MetronomerBot/blob/master/README.md#commands')
async def runall(msg, websocket, userSearch):
   if msg.replace(' ', '').lower() == PM(userSearch, 'spheal'):
      spheal(websocket, userSearch)
   if msg.replace(' ', '').lower() == PM(userSearch, 'commands'):
      commands(websocket, userSearch)