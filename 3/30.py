# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

def GetSentences():
    sentence=[]
    with open ('neko.txt.mecab','r',encoding='utf-8_sig') as f:
        for line in f.readlines():
            if line.strip()=='EOS':
                return
            #line : "吾輩	ワガハイ	吾輩	名詞-代名詞-一般"
            info=line.split('\t') # lineは\tで各要素に区切られる
            tmp=info[3].split('-')
            dic={
                'surface':info[0],
                'base':info[2],
                'pos':tmp[0], #名詞-代名詞-一般のようになっているのでハイフンでsplitして0と1を取り出す
            }
            if len(tmp)>1:
                dic['pos1']=tmp[1]
            else:
                dic['pos1']=None

            sentence.append(dic)
            if dic['surface'] in ['。','　']:
                if len(sentence)>1:
                    yield sentence
                sentence=[]#リストを空にする

output=GetSentences()
print(list(output))