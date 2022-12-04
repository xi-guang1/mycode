from musicpy import *


def btn_play_onclick(note_lst, durlst, durlst_1,save_as_file=False):
    play(chord(note_lst, durlst, durlst_1),bpm=120,save_as_file=save_as_file)