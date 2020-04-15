#行数をカウントせよ．確認にはwcコマンドを用いよ
with open ('popular-names.txt') as f:
    print(len(f.readlines()))
