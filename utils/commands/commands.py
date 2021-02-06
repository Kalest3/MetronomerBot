from config import username
def spheal(user):
   return f'|/pm {user}, spheal'
async def runall(msg, websocket, userSearch):
   if msg == f'|pm| {userSearch}| {username}|@spheal':
      await websocket.send(spheal(user=userSearch))