from showdown.login import *
from battles.awaitbattle import *
from showdown.search import *
partidas = 0
async def confirm():
    global battletagf
    battletag = log.find('gen8metronomebattle-')
    battletag2 = log.find('|')
    battletagf = log[battletag:battletag2]
    battletagf = battletagf.replace('gen8metronomebattle-', '')
    battletagf = battletagf.strip()
    await battleon()
def choosemove():
   return f'battle-gen8metronomebattle-{battletagf}|/choose default'
def timeron():
   return f'battle-gen8metronomebattle-{battletagf}|/timer on'
def leave():
   return f'/noreply |/leave battle-gen8metronomebattle-{battletagf}'
async def battleon():
  await websocket.send(timeron())
  await websocket.send(choosemove())
  while True:
    websocketaw2 = await websocket.recv()
    turn = '|turn|' in websocketaw2
    ladderup = '||Ladder updating' in websocketaw2
    if turn != False:
       c = '|c|' in websocketaw2
       if c != True:
          await websocket.send(choosemove())
       else:
          pass
    elif ladderup != False:
       c = '|c|' in websocketaw2
       if c != True:
          global partidas
          partidas = partidas + 1
          print(partidas)
          if partidas == 150:
             await websocket.send(leave())
             partidas = 0
             sys.exit()
          else:
             await websocket.send(leave())
             await search()
       else:
          pass