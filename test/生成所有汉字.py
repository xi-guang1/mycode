def write():
    with open(r"test\text\UTF-8所有汉字.txt", "w+", encoding="utf-8") as f:
        for u in range(0x4e00, 0x9fbf):
            # f.write(chr(u))
            print(chr(u),end='',file=f)

def read():
    with open(r"test\text\UTF-8所有汉字.txt", "r", encoding="utf-8") as f:
        return f.read()

write()
read()