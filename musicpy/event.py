from musicpy import *


def btn_play_onclick(note_lst, durlst = None, durlst_1 = None):
    play(chord(note_lst, durlst, durlst_1), 120)