from musicpy import *


def btn_play_onclick(note_lst, durlst, durlst_1):
    print(durlst)
    print(durlst_1)
    play(chord(note_lst, durlst, durlst_1))