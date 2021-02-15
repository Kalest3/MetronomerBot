from config import username, owner
def PM(userSearch, command: str):
   return f'|pm|{userSearch}|{username}|@{command}'
def spheal(user: str):
   return f'|/pm {user}, spheal'
def join(room: str):
   return f'|/j {room}'
def leave(room: str):
   return f'{room}|/part'
async def runall(msg, websocket, userSearch):
   if msg.replace(' ', '').lower() == PM(userSearch, 'spheal'):
      await websocket.send(spheal(user=userSearch))
   if msg.replace(' ', '') == PM(userSearch, 'join'):
      if userSearch == owner:
         roomSearch = msg.find('@join')
         room = msg[roomSearch:-1]
         room = room.replace('@join')
         room = room.strip()
         await websocket.send(join(room))
   if msg.replace(' ', '') == PM(userSearch, 'leave'):
      if userSearch == owner:
         roomSearch = msg.find('@leave')
         room = msg[roomSearch:-1]
         room = room.replace('@leave')
         room = room.strip()
         await websocket.send(leave(''))