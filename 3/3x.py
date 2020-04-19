#夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
import MeCab
m = MeCab.Tagger ("-Ochasen")
with open ('neko.txt','r',encoding='utf-8_sig') as f:
    output=m.parse(f.read())

with open ('neko.txt.mecab','w',encoding='utf-8_sig') as f:
    f.write(output)
