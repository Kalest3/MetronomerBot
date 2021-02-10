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
    global battlesid
    global logCons
    loginDone = False
    battleOn = False
    logCons = False
    while True:
        msg = await websocket.recv()
        if msg[0:10] == '|challstr|':
            challstr = msg[0:99999]
            challstr = challstr.replace('|challstr|', '')
            challstr = challstr.strip()
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
            loginDone = True
            battlesid = open('battlesid.txt', 'r+')
            battlesid.seek(0, 0)
            readid = battlesid.readlines()
            ClosedBattle = 'CLOSED' in readid
            if ClosedBattle == False and len(readid) > 0:
                battleOn = True
                logCons = readid[0]
                await websocket.send(f'|/j {logCons}')
            else:
                await search(websocket=websocket)
        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket)
async def onLogin(msg, websocket):
    msg = str(msg)
    if '|pm|' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.replace(' ', '')
        userSearch = userSearch.strip()
        await runall(msg=msg, websocket=websocket, userSearch=userSearch)
    if '|request|' in msg:
        global logCons
        logConsSearch = msg.find('battle-gen8metronomebattle')
        logConsSearch2 = msg.find('\n')
        logCons = msg[logConsSearch:logConsSearch2]
        await verifyBattle(msg, logCons, websocket)
    if battleOn == True:
        battlesid = open('battlesid.txt', 'w+')
        battlesid.write(logCons)
        await on_battle(msg, logCons, websocket, battlesid)