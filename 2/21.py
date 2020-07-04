#記事中でカテゴリ名を宣言している行を抽出せよ．
import json
import re

def GetArticle():
    lst=[]
    with open ('jawiki-country.json','r',encoding='utf-8_sig') as f:
        for line in f.readlines():
            dic=json.loads(line)
            lst.append(dic)

    for dic in lst:
        if dic['title']=='イギリス':
            return dic['text']

for line in GetArticle().split('\n'):
    if re.match(r'\[\[Category:.*\]\]',line):
        print(line)