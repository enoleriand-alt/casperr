import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
import sys
import os

B = """

██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                          

"""
print(B)
print ("")
print(colored('[+] 25 Different working Proxy server Each time :', 'green')) 
print(colored('[+] Starting...', 'green' ))

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=100 ), show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(colored('[+] Done', 'green'))

