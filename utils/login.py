import json
import requests
import battles.battle as battle
from config import *
from typethis import *

async def Login(websocket):
    loginDone = False
    while True:
        msg = str(await websocket.recv())

        if enablelogs:
            """Prints the console messages
            """
            print(msg)

        if msg[0:10] == '|challstr|':
            """Login into the Pokémon Showdown Server
            """
            challstr = msg[10:]
            postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
            assertion = json.loads(postlogin.text[1:])["assertion"]
            await websocket.send(f'|/trn {username},0,{assertion}')
            await websocket.send(f'|/avatar {avatar}')
            await battle.reconnectToBattle(msg, websocket)

            loginDone = True

        if loginDone:
            await afterLogin(msg, websocket)

async def afterLogin(msg, websocket):
    if msg[0:28] == ">battle-gen8metronomebattle-":
        await battle.on_battle(msg, websocket)