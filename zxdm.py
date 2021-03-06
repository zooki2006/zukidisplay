# zuki X display manager for window managers
import os
import argparse
#import subprocess
ver=1.0

def listwm(wmarray):
    x = 0
    for wm in wmarray:
        x += 1
        print(f"[{x}] {wm} ", end = ' ')

def sx(startwm, path):
    print(f"run 'exec {xorg} sh {path}{startwm} in shell'")
    x = f"{xorg} sh {path}{startwm}"
    print(x)
    os.system(x)

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    wmarray = []
    for entry in os.scandir(path):
        if entry.is_file():
            if entry.name != "zdm.conf":
                wmarray.append(entry.name) 
    listwm(wmarray)
    print("[q] quit")
    startwm = input("launch:")
    try:
        val = int(startwm)
        x = len(wmarray)
        if val > x:
            print("user output to big")
            main()
            exit()
        elif val < 1:
            print("user input to small")
            main()
            exit()
        x = wmarray[val - 1]
        sx(x, path)
    except ValueError:
        if startwm == "q":
            quit()
        sx(startwm, path)
def parse_arguments():
    helpmenu = f"a cli display manager using scripts in $HOME/.config/zdm/ as options"
    parser = argparse.ArgumentParser(description = helpmenu)
    parser.add_argument("-v", "--version", help = "display ver num", action="store_true")
    parser.add_argument("-i", "--inputdir", type=str, help = "input custom dir")
    parser.add_argument("-x", "--xinit", help = "use xinit over sx", action="store_true")
    args = parser.parse_args()
    if args.version:
        print(f"zxdm-{ver}")
        exit()
    global path
    global xorg
    if args.xinit:
        xorg = "xinit"
    else:
        xorg = "sx"
    if args.inputdir == None:
        home = os.path.expanduser("~")
        path = (home + "/.config/zdm/") 
    else:
        path = args.inputdir
    makedir(path)

if __name__ == "__main__":
    parse_arguments()
    try:
        main()
    except KeyboardInterrupt:
        print("(Ctrl-C)")
