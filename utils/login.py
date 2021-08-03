import json
import requests
import re
from config import *
from typethis import *

async def Login(websocket):
    global logCons
    global Reconnected
    loginDone = False
    logCons = None

    while True:
        msg = await websocket.recv()
        msg = str(msg)
        print(msg)
        if msg[0:10] == '|challstr|':
            challstr = msg[0:99999]
            challstr = challstr.replace('|challstr|', '')
            challstr = challstr.strip()
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
            import battles.battle as battle
            while True:
                msg = await websocket.recv()
                if '|updatesearch|' in msg:
                    while True:
                        msg = await websocket.recv()

                        if '|updatesearch|' in msg:
                            jsonMSG = msg.replace('|updatesearch|', '')
                            jsonMSGloaded = json.loads(jsonMSG)
                            games = jsonMSGloaded["games"]
                            games = str(games)

                            if games != "None":
                                games = games.split("[Gen 8] Metronome Battle")
                                for item in games:
                                    itemOnlyAlnum = re.sub(r'\W+', '', item)
                                    if itemOnlyAlnum[0:25] == "battlegen8metronomebattle":
                                        await websocket.send(f"|/j battle-gen8metronomebattle-{itemOnlyAlnum[25:]}")
                                Reconnected = True

                            else:
                                await battle.search(websocket)
                                Reconnected = False

                            loginDone = True
        
                            break
                break

        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket, battle=battle)

async def onLogin(msg, websocket, battle):

    if msg[0:28] == ">battle-gen8metronomebattle-":
        await battle.on_battle(msg, websocket)
