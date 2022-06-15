import os
#import subprocess
home = os.path.expanduser("~")
path = (home + "/.config/zwm/") 

def listwm(wmarray):
    x = 0
    for wm in wmarray:
        x += 1
        #if wm == 'zwm.conf':
        #    print('')
        #else:
        print(f"[{x}] {wm} ", end = ' ')

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
    wmarray = os.listdir(path)
    wmarray.remove("zwm.conf")
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
        sxint(val, path, wmarray)
    except ValueError:
        if startwm == "q":
            quit()
        sxstr(startwm, path)
    #sx(startwm, path)
#try:
#    main()
#except KeyboardInterrupt:
#    print("\nKEYBOARDINTERRUPT")
if __name__ == "__main__":
    main()
