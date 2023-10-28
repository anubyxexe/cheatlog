#import
import json
import pystyle
from pystyle import Colors, Colorate, Write
import os

#logo
os.system('cls' if os.name=='nt' else 'clear')
logo = """_________ .__                   __  .____                  
\_   ___ \|  |__   ____ _____ _/  |_|    |    ____   ____  
/    \  \/|  |  \_/ __ \\\\__  \\\\   __\    |   /  _ \ / ___\ 
\     \___|   Y  \  ___/ / __ \|  | |    |__(  <_> ) /_/  >
 \______  /___|  /\___  >____  /__| |_______ \____/\___  / 
        \/     \/     \/     \/             \/    /_____/ V1
"""
print(Colorate.Horizontal(Colors.red_to_blue, logo))
print()

with open("data.json", "r") as files:
    data = json.load(files)

while True:
    search = Write.Input("player name -> ", Colors.red_to_blue, interval=0.05)

    if(search == "exit"):
        break
    elif search in data:
        infos = data[search]
        Write.Print(f"Name: {search}\n", Colors.blue_to_green, interval=0.05)
        #Write.Print(f"level : {infos[0]}\n", Colors.blue_to_green, interval=0.05)
        Write.Print(f"cheat: true\n", Colors.blue_to_green, interval=0.05)
        Write.Print(f"reason: {infos[1]}\n", Colors.blue_to_green, interval=0.05)
        print()
    else:
        Write.Print(f"{search} is not log.", Colors.blue_to_green, interval=0.05)
        print()
