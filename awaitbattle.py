from login import *
async def awaitar():
  while True:
    global websocketaw1
    websocketaw1 = await websocket.recv()
    if '|turn|1' in websocketaw1 != False:
        import battle
        await battle.confirm()