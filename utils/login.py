import json
import requests
import re
import sqlite3
from config import *
from typethis import *

connectCAL = sqlite3.connect("ChallengesAndLadder.db")
cursorCAL = connectCAL.cursor()

try:
    cursorCAL.execute("CREATE TABLE challengeActives(battleid TEXT)")
    cursorCAL.execute("CREATE TABLE ladderActives(battleid TEXT)")
    cursorCAL.execute("CREATE TABLE challenge(battleid TEXT)")
    cursorCAL.execute("CREATE TABLE ladder(battleid TEXT)")
except:
    pass

async def Login(websocket):
    global logCons
    global Reconnected
    loginDone = False
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

                            if games != "None":
                                games = games.split("[Gen 8] Metronome Battle")
                                for item in games:
                                    itemOnlyAlnum = re.sub(r'\W+', '', item)
                                    if itemOnlyAlnum[0:25] == "battlegen8metronomebattle":
                                        await websocket.send(f"|/j battle-gen8metronomebattle-{itemOnlyAlnum[25:]}")
                                Reconnected = True

                            else:
                                Reconnected = False

                            cursorCAL.execute("SELECT * FROM ladderActives")
                            if len(cursorCAL.fetchall()) > 0:
                                pass
                            else:
                                import battles.battle
                                await battles.battle.search(websocket)
                            loginDone = True
        
                            break
                break

        if loginDone != False:
            await onLogin(msg=msg, websocket=websocket)

async def onLogin(msg, websocket):
    global battleOn

    if msg[0:28] == ">battle-gen8metronomebattle-":
        import battles.battle
        await battles.battle.on_battle(msg, websocket, cursorCAL, connectCAL)

    if len(msg.split("|")) > 4:
        if msg.split("|")[4] == "/challenge gen8metronomebattle":
            import battles.battle
            await utm(websocket, battles.battle.teamChoice())
            await accept(websocket, msg.split("|")[2])