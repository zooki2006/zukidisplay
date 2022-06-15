import os


def listwm(wmarray):
    x = 0
    for wm in wmarray:
        x += 1
        if wm == 'zwm.conf':
            print('')
        else:
            print(f"[{x}] {wm} ", end = ' ')


def sxstr(startwm, path):
    print(f"run 'exec sx sh {path}{startwm} in shell'")

def sxint(startwm, path, wmarray):
    x = wmarray[startwm - 1]
    print(f"run 'exec sx sh {path}{x} in shell'")


def main():
    home = os.path.expanduser("~")
    path = (home + "/.config/zwm/") 
    wmarray = os.listdir(path)
    listwm(wmarray)
    startwm = input("launch:")
    try:
        val = int(startwm)
        sxint(val, path, wmarray)
    except ValueError:
        sxstr(startwm, path)
    #sx(startwm, path)
try:
    main()
except KeyboardInterrupt:
    print("\nKEYBOARDINTERRUPT")
