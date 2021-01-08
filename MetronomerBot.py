import json
import websockets
import requests
import asyncio
import sys
import random
with open(r'username oficial do metronomer.txt') as u:
    username1 = u.read()
with open(r'senha oficial do metronomer.txt') as p:
    password1 = p.read()
sys.setrecursionlimit(2000)
partidas = 0
async def connect():
    uri = 'ws://sim.smogon.com:8000/showdown/websocket'
    global websocket
    async with websockets.connect(uri) as websocket:
        await login()
async def login():
        while True:
            msg = await websocket.recv()
            msg = str(msg)
            if 'challstr' in msg != False:
                challstr = msg[0:99999]
                challstr = challstr.replace('|challstr|', '')
                challstr = challstr.strip()
                postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username1,'pass':password1,'challstr':challstr})
                assertion = json.loads(postlogin.text[1:])["assertion"]
                await websocket.send(f'|/trn {username1},164,{assertion}')
                await websocket.send('|/avatar 164')
                await websocket.send('|/blockpms')
                await search()
async def search():
        teams = []
        teamstxt = open('teams.txt', 'r')
        read = teamstxt.readlines()
        for ler in read:
          teams.append(ler.strip())
        choice = random.choice(teams)
        await websocket.send(f'|/utm {choice}')
        await websocket.send('|/search gen8metronomebattle')
        await awaitar()
async def awaitar():
    while True:
        global websocketaw1
        websocketaw1 = await websocket.recv()
        if '|turn|1' in websocketaw1 != False:
            await confirm()
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
    await ataque()
async def ataque():
    await websocket.send(f'battle-gen8metronomebattle-{battletagf}|/choose default')
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
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())