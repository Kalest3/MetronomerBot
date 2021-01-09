from login import *
from awaitbattle import *
from search import *
partidas = 0
async def confirm():
    global battletagf
    battletag = websocketaw1.find('gen8metronomebattle-')
    battletag2 = websocketaw1.find('|')
    battletagf = websocketaw1[battletag:battletag2]
    battletagf = battletagf.replace('gen8metronomebattle-', '')
    battletagf = battletagf.strip()
    await websocket.send(f'battle-gen8metronomebattle-{battletagf}|Hi! Im a bot that plays Metronome Battles. If you find any error, send a PM to the user Gabriel Gottapok with the link for this match.')
    await timeron()
async def timeron():
    await websocket.send(f'battle-gen8metronomebattle-{battletagf}|/timer on')
    await websocket.send(f'battle-gen8metronomebattle-{battletagf}|/choose default')
    await ataque()
async def ataque():
  while True:
    websocketaw2 = await websocket.recv()
    turn = '|turn|' in websocketaw2
    ladderup = '||Ladder updating' in websocketaw2
    if turn != False:
       c = '|c|' in websocketaw2
       if c != True:
          await websocket.send(f'battle-gen8metronomebattle-{battletagf}|/choose default')
       else:
          pass
    elif ladderup != False:
       c = '|c|' in websocketaw2            
       if c != True:
          global partidas
          partidas = partidas + 1
          print(partidas)          
          if partidas == 150:
             await websocket.send(f'/noreply |/leave battle-gen8metronomebattle-{battletagf}')
             partidas = 0
             sys.exit()
          else:
             await websocket.send(f'/noreply |/leave battle-gen8metronomebattle-{battletagf}')
             await search()
       else:
          pass