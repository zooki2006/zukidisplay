# zuki display manager for window managers
import os
import argparse
#import subprocess
ver=0.9

def listwm(wmarray):
    x = 0
    for wm in wmarray:
        x += 1
        print(f"[{x}] {wm} ", end = ' ')

def way(startwm, waypath):
    y = f"sh {waypath}{startwm}"
    print(y)
    os.system(y)

def sx(startwm, path):
    x = f"sx sh {path}{startwm}"
    print(x)
    os.system(x)


def sxstr(startwm, path):
    print(f"run 'exec sx sh {path}{startwm} in shell'")
    sx(startwm, path)

def sxint(startwm, path, wmarray):
    x = wmarray[startwm - 1]
    print(f"run 'exec sx sh {path}{x} in shell'")
    sx(x, path)

def main():
    #wmarray = os.listdir(path)
    xwmarray = []
    ywmarray = []
    ywmprint = []
    xwmprint = []
    for entry in os.scandir(path):
        if entry.is_file():
            if entry.name != "zdm.conf":
                xwmarray.append(entry.name) 
                xwmprint.append(f"(x){entry.name}") 
    for entry in os.scandir(waypath):
        if entry.is_file():
            ywmarray.append(entry.name) 
            ywmprint.append(f"(w){entry.name}") 
    wmarray = xwmarray + ywmarray
    wmprint = xwmprint + ywmprint
    if typeindicator:
        listwm(wmprint)
    else:
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
        if x in ywmarray:
            way(x, waypath)
        else:
            #sxint(val, path, wmarray)
            sxstr(startwm, path)
    except ValueError:
        if startwm == "q":
            quit()
        sxstr(startwm, path)
    #sx(startwm, path)
#try:
#    main()
#except KeyboardInterrupt:
#    print("\nKEYBOARDINTERRUPT")
def parse_arguments():
    helpmenu = f"a cli display manager using scripts in $HOME/.config/zdm/ (for xorg wm) and $HOME/.config/zdm/way/ (for wayland wm) as options"
    parser = argparse.ArgumentParser(description = helpmenu)
    parser.add_argument("-v", "--version", help = "display ver num", action="store_true")
    parser.add_argument("-i", "--inputdir", type=str, help = "input custom dir")
    parser.add_argument("-t", "--typeindicator", help = "display session type (x) for xorg (w) for wayland ", action="store_true")
    args = parser.parse_args()
    if args.version:
        print(f"zdm-{ver}")
        exit()
    global path
    global waypath
    global typeindicator
    if args.inputdir == None:
        home = os.path.expanduser("~")
        path = (home + "/.config/zdm/") 
    else:
        path = args.inputdir
    typeindicator = args.typeindicator

    waypath = (f"{path}way/")

if __name__ == "__main__":
    parse_arguments()
    try:
        main()
    except KeyboardInterrupt:
        print("(Ctrl-C)")
