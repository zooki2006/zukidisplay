# zuki display manager for window managers
import os
import argparse
ver=1.0

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
    print(f"run 'exec {xorg} sh {path}{startwm} in shell'")
    x = f"{xorg} sh {path}{startwm}"
    print(x)
    os.system(x)

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    xwmarray = []
    ywmarray = []
    ywmprint = []
    xwmprint = []
    for entry in os.scandir(path):
        if entry.is_file():
            if entry.name != "Xsession":
                xwmarray.append(entry.name) 
                xwmprint.append(f"(x){entry.name}") 
    for entry in os.scandir(waypath):
        if entry.is_file():
            if entry.name != "Wsession":
                ywmarray.append(entry.name) 
                ywmprint.append(f"(w){entry.name}") 
    wmarray = xwmarray + ywmarray
    wmprint = xwmprint + ywmprint
    if typeindicator:
        y = wmprint
    else:
        y = wmarray
    grabwm(wmarray, ywmarray, y)
    
def grabwm(wmarray, ywmarray, wmprint):
    listwm(wmprint)
    print("[q] quit")
    startwm = input("launch:")
    try:
        val = int(startwm)
        x = len(wmarray)
        if val > x:
            print("user output to big")
            grabwm(wmarray, ywmarray, wmprint)
            exit()
        elif val < 1:
            print("user input to small")
            grabwm(wmarray, ywmarray, wmprint)
            exit()
        x = wmarray[val - 1]
        if x in ywmarray:
            way(x, waypath)
        else:
            sx(x, path)
    except ValueError:
        if startwm == "q":
            quit()
        sx(startwm, path)

def parse_arguments():
    helpmenu = f"a cli display manager using scripts in $HOME/.config/zdm/ (for xorg wm) and $HOME/.config/zdm/way/ (for wayland wm) as options"
    parser = argparse.ArgumentParser(description = helpmenu)
    parser.add_argument("-v", "--version", help = "display ver num", action="store_true")
    parser.add_argument("-i", "--inputdir", type=str, help = "input custom dir")
    parser.add_argument("-iw", "--inputwaydir", type=str, help = "input custom wayland dir")
    parser.add_argument("-t", "--typeindicator", help = "display session type (x) for xorg (w) for wayland ", action="store_true")
    parser.add_argument("-x", "--xinit", help = "use xinit over sx", action="store_true")
    args = parser.parse_args()
    if args.version:
        print(f"zdm-{ver}")
        exit()
    global path
    global waypath
    global typeindicator
    global xorg
    if args.inputdir == None:
        home = os.path.expanduser("~")
        path = (home + "/.config/zdm/") 
    else:
        path = args.inputdir
    makedir(path)
    typeindicator = args.typeindicator
    if args.xinit:
        xorg = "xinit"
    else:
        xorg = "sx"
    if args.inputwaydir == None:
        waypath = (f"{path}way/")
    else:
        waypath = args.inputwaydir
    makedir(waypath)


if __name__ == "__main__":
    parse_arguments()
    try:
        main()
    except KeyboardInterrupt:
        print("(Ctrl-C)")
