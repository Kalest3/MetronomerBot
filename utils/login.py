import json
import requests
import asyncio
import websockets
from config import *
from utils.commands.commands import *
from utils.commands.typethis import *
from battles.battle import *
async def Login(websocket):
    global battleOn
    global logCons
    global Reconnected
    loginDone = False
    battleOn = False
    logCons = None
    while True:
        msg = await websocket.recv()
        msg = str(msg)
        if msg[0:10] == '|challstr|':
            challstr = msg[0:99999]
            challstr = challstr.replace('|challstr|', '')
            challstr = challstr.strip()
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
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
                            if games == "None":
                                Reconnected = False
                                await search(websocket=websocket)
                            else:
                                startSearch = games.find("'", 1)
                                endSearch = games.find("'", 2)
                                battle = games[startSearch:endSearch]
                                battle = battle.replace("'", '')
                                await websocket.send(f'|/join {battle}')
                                logCons = battle
                                battleOn = True
                                Reconnected = True
                            loginDone = True
                            break
                break
        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket)
async def onLogin(msg, websocket):
    if '|pm|' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.replace(' ', '')
        userSearch = userSearch.lower()
        userSearch = userSearch.strip()
        await runall(msg=msg, websocket=websocket, userSearch=userSearch)
    if '|request|' in msg and battleOn == False:
        global logCons
        logConsSearch = msg.find('battle-gen8metronomebattle')
        logConsSearch2 = msg.find('\n')
        logCons = msg[logConsSearch:logConsSearch2]
        await verifyBattle(msg, logCons, websocket)
    if battleOn == True:
        await on_battle(msg, logCons, websocket)