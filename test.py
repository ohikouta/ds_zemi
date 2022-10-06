# -*- coding:utf-8 -*-

from word_count import *

var_list = ["var1", "var2", "var3"]
var_list = columns_list

tiger = 50

for i in range(len(var_list)):
    var_name = var_list[i] + "_dict"
    exec("{} = tiger".format(var_name))
    

# ['ntt', 'panasonic', 'kddi', 'hitachi', 'fujitsu', 'cyberagent', 'softbank', 'sony', 'rakuten']

all_freq_word = []
for dict in all_dict_list:
    freq_word = {}
    dict_values = list(dict.values())
    freq_count = [i for i in dict_values if i >= 2]
    print(len(freq_count))
    print(freq_count)
    count = 0
    freq_word = {}
    print(len(dict))
    for word in dict:
        count += 1
        
        if dict[word] >= 2:
            freq_word[word] = dict[word]
    print("=" * 100)
    print(len(freq_word))
    all_freq_word.append(freq_word)
    print("=" * 100)
            

    print(count)

print(len(all_freq_word))

for i in range(len(all_freq_word)):
    print(all_freq_word[i])
        
# 2回以上の出現回数を持つ単語の辞書を作成した．

# 9つの辞書(各IT企業統合報告書目次において2回以上出現した単語の辞書)
freq_ntt_dict = all_freq_word[0]
freq_panasonic_dict = all_freq_word[1]
freq_kddi_dict = all_freq_word[2]
freq_hitachi_dict = all_freq_word[3]
freq_fujitsu_dict = all_freq_word[4]
freq_cyberagent_dict = all_freq_word[5]
freq_softbank_dict = all_freq_word[6]
freq_sony_dict = all_freq_word[7]
freq_rakuten_dict = all_freq_word[8]




