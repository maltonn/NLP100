#動詞の表層形をすべて抽出せよ．
with open ('neko.txt.mecab','r',encoding='utf-8_sig') as f:
    st=set()
    for line in f.readlines():
        line=line.split('\t')

        if len(line)!=6:
            continue
        
        if '動詞' in line[3]:
            st.add(line[0])

    print(st)
