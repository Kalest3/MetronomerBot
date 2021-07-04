from string import digits
from utils import login
from typethis import *

async def search(websocket):
    await utm(websocket, teamChoice())
    await laddersearch(websocket)

async def on_battle(msg, websocket, cursorCAL, connectCAL):
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

    if lastmsg == "|turn|1":
        if "|rated|" in msg:
            cursorCAL.execute("INSERT INTO ladder VALUES(?)", (logCons,))
            cursorCAL.execute("INSERT INTO ladderActives VALUES(?)", (logCons,))
        else:
            cursorCAL.execute("INSERT INTO challenge VALUES(?)", (logCons,))
            cursorCAL.execute("INSERT INTO challengeActives VALUES(?)", (logCons,))
        connectCAL.commit()

    if lastmsgWithoutDigits == '|turn|':
        await choosemove(websocket, logCons)

    if lastmsgWithoutDigits[0:5] == '|win|':
        await leave(websocket, logCons)
        cursorCAL.execute("SELECT * FROM ladderActives")
        if f"('{logCons}',)," or f"[('{logCons}',)," or f"('{logCons}',)]" in str(cursorCAL.fetchall()):
            cursorCAL.execute("DELETE FROM ladderActives WHERE battleid = ?", (logCons,))
            await search(websocket)
        else:
            cursorCAL.execute("DELETE FROM challengeActives WHERE battleid = ?", (logCons,))
        connectCAL.commit()

    if login.Reconnected == True:
        await choosemove(websocket, logCons)
        login.Reconnected = False