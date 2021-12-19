from Rem import Rem
import asyncio

rem = Rem()
loop = asyncio.get_event_loop()
loop.run_until_complete(rem.main_loop())
loop.close()