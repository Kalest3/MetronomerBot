from login import *
async def awaitar():
  while True:
    global websocketaw1
    global log
    websocketaw1 = await websocket.recv()
    if '|turn|1' in websocketaw1 != False:
        log = websocketaw1
        import battle
        battle.log = log
        await battle.confirm()