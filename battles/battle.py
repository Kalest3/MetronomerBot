from sqlite3.dbapi2 import connect
from string import digits
from utils import login
from typethis import *
import sqlite3

connectCAL = sqlite3.connect("ChallengesAndLadder.db")
cursorCAL = connectCAL.cursor()


async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket):
    logConsSearch = msg.find('battle-gen8metronomebattle')
    logConsSearch2 = msg.find('\n')
    logCons = msg[logConsSearch:logConsSearch2]
    if msg == f'>{logCons}\n|request|':
        await timeron(websocket, logCons)
        await choosemove(websocket, logCons)
    splitws = msg.splitlines()
    if '|upkeep' in splitws != False:
        splitws.remove('|upkeep')
    lastmsg = splitws[-1]
    remove_digits = str.maketrans('', '', digits)
    lastmsgWithoutDigits = lastmsg.translate(remove_digits)
    try:
        if msg[0:28] == ">battle-gen8metronomebattle-":
            if lastmsg == "|turn|1":
                if "|rated|" in msg:
                    cursorCAL.execute("INSERT INTO ladder VALUES(?)", (logCons,))
                else:
                    cursorCAL.execute("INSERT INTO challenge VALUES(?)", (logCons,))
                connectCAL.commit()
            if lastmsgWithoutDigits == '|turn|':
                await choosemove(websocket, logCons)
            if lastmsgWithoutDigits[0:5] == '|win|':
                await leave(websocket, logCons)
                cursorCAL.execute("SELECT * FROM ladder")
                for battle in cursorCAL.fetchall():
                    battle = str(battle)
                    if battle == f"('{logCons}',)":
                        print("hello")
                        cursorCAL.execute("DELETE FROM ladder")
                        connectCAL.commit()
                        await search(websocket)
                    else:
                        pass
            if login.Reconnected == True:
                await choosemove(websocket, logCons)
                login.Reconnected = False
    except:
        pass