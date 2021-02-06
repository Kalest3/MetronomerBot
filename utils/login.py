import json
import websockets
import requests
import asyncio
import sys
import random
import threading
from config import *
from utils.commands.commands import *
from utils.commands.typethis import *
from battles.battle import *
sys.setrecursionlimit(2000)
async def Login(websocket):
    global battleOn
    loginDone = False
    battleOn = False
    while True:
        msg = await websocket.recv()
        if 'challstr' in msg != False:
            challstr = msg[0:99999]
            challstr = challstr.replace('|challstr|', '')
            challstr = challstr.strip()
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
            loginDone = True
            await search(websocket=websocket)
        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket)
async def onLogin(msg, websocket):
    global logCons
    msg = str(msg)
    if '|pm|' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.strip()
        await runall(msg=msg, websocket=websocket, userSearch=userSearch)
    if '|request|' in msg:
        logConsSearch = msg.find('battle-gen8metronomebattle')
        logConsSearch2 = msg.find('\n')
        logCons = msg[logConsSearch:logConsSearch2]
        await verifyBattle(msg, logCons, websocket)
    if battleOn == True:
        await on_battle(msg, logCons, websocket)