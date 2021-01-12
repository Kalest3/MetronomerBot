import showdown.login as login
import asyncio
class run():
    def __init__(self):
        asyncio.get_event_loop().run_until_complete(login.connect())
if __name__ == "__main__":
    runMetro: run = run()