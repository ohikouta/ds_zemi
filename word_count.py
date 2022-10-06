# -*- coding:utf-8 -*-

import pandas as pd
from janome.tokenizer import Tokenizer


# データの読み込み
df_contents = pd.read_csv("C:\\Users\\81804\\OneDrive - cuc.ac.jp\\annual_contents\\contents.csv")

# データのカラムをリストに変換
columns_list = list(df_contents.columns)

# 列ごとにリストを作成する
contents_list = []

for i in columns_list:
    contents_list.append(list(df_contents[i]))

# 列ごとのリストを1つのテキストに変換
contents_text = []

for i in range(len(columns_list)):
    text = ''.join(map(str, contents_list[i]))
    contents_text.append(text)
    
    
# ここまでで目次をテキストデータとして収集した。
# 続いてトークナイザで単語分割，頻出単語を可視化するか，その前に前処理を行うか
# 前処理を行うなら，とりあえず括弧とnanを消したい．

for i in range(len(contents_text)):
    contents_text[i] = contents_text[i].replace("nan", "")
    contents_text[i] = contents_text[i].replace("（", "")
    contents_text[i] = contents_text[i].replace("）", "")
    
# janomeを使って単語分割
from janome.tokenizer import Tokenizer
t = Tokenizer()
s = 'すもももももももものうち'
print(type(t.tokenize(s)))

for token in t.tokenize(s):
    print(token)
    
print(list(t.tokenize(s, wakati=True)))
text_list = list(t.tokenize(s, wakati=True))
print(len(text_list))

# それぞれのテキストを単語で分割したリストに変換したい．

all_word_list = []
unique_word_list = []
all_count = []
for text in contents_text:
    # contents_textの各要素をtext_listに変換する(text_list=単語集)
    text_list = list(t.tokenize(text, wakati=True))
    unique_word_list.append(list(set(text_list)))
    all_word_list.append(text_list)
    all_count.append(len(text_list))


print(len(all_word_list))
print(len(unique_word_list))
unique_count = [len(i) for i in unique_word_list]

# 中身の確認 len=9
print("All word count:\n{}".format(all_count))
print("Unique word count:\n{}".format(unique_count))

# ユニークな単語のリストをイテレータとして
# それぞれ目次に登場した単語を辞書化して保存→これが可視化の元となるデータ{"word": 00}

all_dict_list = []

var_list = columns_list
for idx in range(len(contents_text)):
    # word_dict: このループ内だけで使用する変数
    # 形式 {"word": 00}
    # これを9つ作成する．
    word_dict = {} 
    for word in unique_word_list[idx]:
        word_dict[word] = all_word_list[idx].count(word)
    
    # 最後にall_dict_listに単語出現回数が格納された辞書が9つ格納される．
    all_dict_list.append(word_dict)
    

print(len(all_dict_list))

# ===================================================================
# ここから出現回数が2回以上の単語のみ辞書に残す
# 1回だけ出現しているものは意味がないとみなす．
all_freq_word = []
for dict in all_dict_list:
    freq_word = {}
    dict_values = list(dict.values())
    freq_count = [i for i in dict_values if i >= 2]
    # 2回以上出現した単語は何個あるか確認
    print(len(freq_count))

    for word in dict:
        # 2回以上出現した単語のみfreq_word{}に格納
        if dict[word] >= 2:
            freq_word[word] = dict[word]
    all_freq_word.append(freq_word)
        
# 2回以上の出現回数を持つ単語の辞書を作成した．

# 9つの辞書(各IT企業統合報告書目次において2回以上出現した単語の辞書)
# それぞれの辞書を対応する企業名の入った変数に格納する．
freq_ntt_dict = all_freq_word[0]
freq_panasonic_dict = all_freq_word[1]
freq_kddi_dict = all_freq_word[2]
freq_hitachi_dict = all_freq_word[3]
freq_fujitsu_dict = all_freq_word[4]
freq_cyberagent_dict = all_freq_word[5]
freq_softbank_dict = all_freq_word[6]
freq_sony_dict = all_freq_word[7]
freq_rakuten_dict = all_freq_word[8]

# 最終確認
all_dict = []
all_dict.append(freq_ntt_dict)
all_dict.append(freq_panasonic_dict)
all_dict.append(freq_kddi_dict)
all_dict.append(freq_hitachi_dict)
all_dict.append(freq_fujitsu_dict)
all_dict.append(freq_cyberagent_dict)
all_dict.append(freq_softbank_dict)
all_dict.append(freq_sony_dict)
all_dict.append(freq_rakuten_dict)

for data in all_dict:
    print("=" * 100)
    print(data)
    print("=" * 100)



    
        
    


