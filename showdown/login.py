import json
import websockets
import requests
import asyncio
import sys
import random
with open(r'username.txt') as u:
    username1 = u.read()
with open(r'password.txt') as p:
    password1 = p.read()
sys.setrecursionlimit(2000)
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
                import showdown.search as search
                await search.search()