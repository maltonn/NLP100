# News Aggregator Data Setをダウンロードし、以下の要領で学習データ（train.txt），検証データ（valid.txt），評価データ（test.txt）を作成せよ．

import time
start = time.time()

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# ダウンロードしたzipファイルを解凍し，readme.txtの説明を読む．
df = pd.read_table('data/newsCorpora.csv', header=None)
df.columns = ['ID', 'TITLE', 'URL', 'PUBLISHER',
              'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']

# 情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
df['PUBLISHER'] = df['PUBLISHER'].fillna('')
df = df[df['PUBLISHER'].str.match(
    '(Reuters|Huffington Post|Businessweek|Contactmusic.com|Daily Mail)')]

# 抽出された事例をランダムに並び替える．
# 抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ（このファイルは後に問題70で再利用する）．
train_df, non_train_df = train_test_split(df, test_size=0.2)
valid_df, test_df = train_test_split(non_train_df, test_size=0.5)

train_df.to_csv('dataset/train.txt', sep='\t')
valid_df.to_csv('dataset/valid.txt', sep='\t')
test_df.to_csv('dataset/test.txt', sep='\t')


# 学習データと評価データを作成したら，各カテゴリの事例数を確認せよ．
id_to_category={
    'b':'business',
    't':'science and technology',
    'e':'entertainment',
    'm':'health'
}

for cat in sorted(list(set(df['CATEGORY']))):
    print('{}\t: {}'.format(id_to_category[cat],np.count_nonzero(df['CATEGORY']==cat)))

print('\n{:.2f} sec'.format(time.time()-start))