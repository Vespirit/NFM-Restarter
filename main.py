from gui import *
from tkinter import filedialog

def openfile() -> str:
    return filedialog.askdirectory()

def restart_game(game: int, path: str) -> None:
    with open(path + "/data/user.data", "r") as f:
        lines = f.readlines()
    
    lines[game + 1] = "NFM" + str(game) + "(0,1)\n"

    with open(path + "/data/user.data", "w") as f:
        f.writelines(lines)


if __name__ == '__main__':
    initModules()
    while isRunning():
        run()