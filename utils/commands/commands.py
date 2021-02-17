from config import username, owner

def PM(userSearch, command: str):
   return f'|pm|{userSearch}|{username}|@{command}'
def spheal(user: str):
   return f'|/pm {user}, spheal'
def commands(user: str):
   return f'|/pm {user}, See my commands at: https://github.com/Kalest3/MetronomerBot/blob/master/README.md#commands'
async def runall(msg, websocket, userSearch):
   global owner
   global username
   owner = owner.replace(' ', '')
   owner = owner.lower()
   username = username.replace(' ', '')
   username = username.lower()
   if msg.replace(' ', '').lower() == PM(userSearch, 'spheal'):
      await websocket.send(spheal(user=userSearch))
   if msg.replace(' ', '').lower() == PM(userSearch, 'commands'):
      await websocket.send(commands(user=userSearch))