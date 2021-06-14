import json
import requests
import re
from config import *
from typethis import *
import sqlite3

connectCAL = sqlite3.connect("ChallengesAndLadder.db")
cursorCAL = connectCAL.cursor()

try:
    cursorCAL.execute("CREATE TABLE challenge(battleid TEXT)")
    cursorCAL.execute("CREATE TABLE ladder(battleid TEXT)")
except:
    pass

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
                            if games != "None":
                                games = games.split("[Gen 8] Metronome Battle")
                                for item in games:
                                    itemOnlyAlnum = re.sub(r'\W+', '', item)
                                    if itemOnlyAlnum[0:25] == "battlegen8metronomebattle":
                                        await websocket.send(f"|/j battle-gen8metronomebattle-{itemOnlyAlnum[25:]}")
                                battleOn = True
                                Reconnected = True
                            else:
                                Reconnected = False
                            cursorCAL.execute("SELECT * FROM ladder")
                            if len(cursorCAL.fetchall()) >= 1:
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
    if '|pm|' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.replace(' ', '')
        userSearch = userSearch.lower()
        userSearch = userSearch.strip()
        import utils.commands.commands as command
        await command.runall(msg=msg, websocket=websocket, userSearch=userSearch)
    if '|request|' in msg and battleOn == False:
        if msg[0:7] == ">battle":
            battleOn = True
    if battleOn == True:
        import battles.battle
        await battles.battle.on_battle(msg, websocket)
    if len(msg.split("|")) > 4:
        if msg.split("|")[4] == "/challenge gen8metronomebattle":
            import battles.battle
            await utm(websocket, battles.battle.teamChoice())
            await accept(websocket, msg.split("|")[2])