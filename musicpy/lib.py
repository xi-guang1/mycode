from musicpy import *
from typing import *

a1 = note("C",5)
a2 = note("D",5)
a3 = note("E",5)
a4 = note("F",5)
a5 = note("G",5)
a6 = note("A",5)
a7 = note("B",5)

a1_ = note("C",6)
a2_ = note("D",6)
a3_ = note("E",6)
a4_ = note("F",6)
a5_ = note("G",6)
a6_ = note("A",6)
a7_ = note("B",6)

a1__ = note("C",4)
a2__ = note("D",4)
a3__ = note("E",4)
a4__ = note("F",4)
a5__ = note("G",4)
a6__ = note("A",4)
a7__ = note("B",4)


def str_to_list(string: str) -> List[note]:
    res = []
    for s in string.split():
        if len(s) == 1:
            res.append(eval(f'a{s}'))
        elif len(s) == 2:
            res.append(eval(f'a{s[0]}_'))
        else:
            res.append(eval(f'a{s[0]}__'))
    return res
