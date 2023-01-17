import jieba
import wordcloud
excludes = {}

#导入txt文件
f = open(r"test\test.txt", "r", encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = r"test\font\SIMKAI.TTF"
    )
w.generate(txt)
w.to_file(r"test\images\tswordcloudm.png")
