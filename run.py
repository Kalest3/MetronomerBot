import asyncio
import websockets
from utils.login import Login
uri = 'ws://sim.smogon.com:8000/showdown/websocket'
async def run():
    async with websockets.connect(uri) as websocket:
        await Login(websocket)
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())