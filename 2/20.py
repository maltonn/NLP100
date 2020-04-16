#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
import json

lst=[]
with open ('jawiki-country.json','r',encoding='utf-8_sig') as f:
    for line in f.readlines():
        dic=json.loads(line)
        lst.append(dic)

for dic in lst:
    if dic['title']=='イギリス':
        print(dic['text'])


