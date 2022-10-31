# -*- coding:utf-8 -*-

import pandas as pd
import sys
sys.path.append("..")
# csv読み込み
df_cyber = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\cyberagent.csv")
df_fujitsu = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\fujitsu.csv")
df_hitachi = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\hitachi.csv")
df_kddi = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\kddi.csv")
df_ntt = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\ntt.csv")
df_panasonic = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\panasonic.csv")
df_rakuten = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\rakuten.csv")
df_softbank = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\softbank.csv")
df_sony = pd.read_csv("C:\\Users\\81804\\working_directory\\zemi\\finance_data\\sony.csv")


data_list = [df_cyber, df_fujitsu, df_hitachi, df_kddi, df_ntt, df_panasonic, df_rakuten, df_softbank, df_sony]


        
# dataframe index 設定        
for i in data_list:
    i.set_index("決算年度", inplace=True)
    

# データフレームに列["付加価値"]を追加する
for df in data_list:
    uriage = "売上高"
    urigen = "売上原価"
    if (type(df.at[2020, uriage]) is str) or (type(df.at[2020, urigen]) is str):
        df["付加価値"] = "計算不可"
    else:
        df["付加価値"] = df["売上高"] - df["売上原価"]

# データフレームに["売上高増加率"], ["利益増加率"], ["総資産増加率"], ["純資産増加率"], ["従業員増加率"]列を追加

new_col_list = {
    "売上高増加率": "売上高",
    "利益増加率": "純利益率",
    "総資産増加率": "総資産",
    "純資産増加率": "純資産",
    "従業員増加率": "従業員数"
    }
for col in new_col_list:
    for df in data_list:
        value = []
        for idx in range(df.shape[0]):
            try:
                calc_result = df.iat[idx, list(df.columns).index(new_col_list.get(col))] / \
                df.iat[idx+1, list(df.columns).index(new_col_list.get(col))]
            except IndexError:
                calc_result = "前年度データなし"
            except TypeError:
                calc_result = "前年度データなし"
            value.append(calc_result)
        df[col] = value


check_columns = []
columns_list = list((data_list[0].columns))

# データフレームの各カラムが同じ内容であるか確認
# ck = [val == columns_list for val in check_columns]


# 求めたい財務指標

profit_finance_index = ["ROA", "ROE", "売上高総利益率", "売上高営業利益率", 
                        "売上高経常利益率", "売上高販管費率"] # 都合上計算できる指標
safety_finance_index = ["流動比率", "固定比率", "自己資本比率"] # 都合上計算できる指標
# safety_finance_index = ["流動比率", "当座比率", "固定比率", "自己資本比率", 
#                         "インタレスト・カバレッジ・レシオ"] # 本来の指標リスト
product_finance_index = ["労働生産性", "資本生産性"] # 都合上計算できる指標
# product_finance_index = ["労働生産性", "資本生産性", "労働分配率"] # 本来の指標リスト
growth_finance_index = ["売上高増加率", "利益増加率", "純資産増加率",
                        "従業員増加率", "EPS"] 
activity_finance_index = ["総資本回転率", "固定資産回転率"] # 都合上計算できる指標
# activity_finance_index = ["総資本回転率", "固定資産回転率", "棚卸資産回転率"] # 本来の指標リスト

finance_class = [profit_finance_index, safety_finance_index, product_finance_index, growth_finance_index, activity_finance_index]

# 分類→calc_possible or calc_impossible
calc_possible = []
calc_impossible = []

def check_calc_possible(finance_class, calc_possible, calc_impossible):
    for i in finance_class:
        possible = []
        impossible = []
        for j in i:
            if j in columns_list:
                possible.append(j)
            else:
                impossible.append(j)
        calc_possible.append(possible)
        calc_impossible.append(impossible)
    return calc_possible, calc_impossible
    
result = check_calc_possible(finance_class, calc_possible, calc_impossible)

print(calc_possible)
        
    
# calc_possible ================================================================================
# get_easy: calc_possibleと判断された値を格納する
def get_easy(calc_possible):
    result_calc_possible = []  # 指標の種類ごと
    for type in calc_possible:
        idx_value = {}  # {"指標名": 9x}
        for idx_name in type:
            value = []  # 各指標の値
            for k in data_list:
                value.append(k.at[2020, idx_name])
            idx_value[idx_name] = value
        result_calc_possible.append(idx_value)
    return result_calc_possible

result_calc_possible = get_easy(calc_possible)
print(result_calc_possible)
        
# 指標を求めるために計算する値のindexをcolumns_listから取り出し,変数に入れる (関数化したい)

# 収益性---------------------------------------------
uriage = columns_list.index("売上高")
eigyo_pr = columns_list.index("営業利益")
keijo_pr = columns_list.index("経常利益")
hankan = columns_list.index("販管費")
# --------------------------------------------収益性
# 安全性--------------------------------------------
# 当座比率は保留
jikoshihon = columns_list.index("自己資本")
koteishisan = columns_list.index("固定資産")
# --------------------------------------------安全性
# 生産性 -------------------------------------------
# 付加価値:売上高-売上原価
add_value = columns_list.index("付加価値")
employee = columns_list.index("従業員数")
# --------------------------------------------生産性
# 成長性 -------------------------------------------

# --------------------------------------------成長性
# 活動性 ------------------------------------------
soshisan = columns_list.index("総資産")
# --------------------------------------------活動性

finance_class_name = ["profit", "safety", "product", "growth", "activity"]
use_idx_profit = {"売上高": uriage, "営業利益": eigyo_pr, "経常利益": keijo_pr, "販管費": hankan}
use_idx_safety = {"自己資本": jikoshihon, "固定資産": koteishisan}
use_idx_product = {"付加価値": add_value, "従業員数": employee, "総資産": soshisan}
# use_idx_growth
use_idx_activity = {"固定資産": koteishisan, "売上高": uriage, "総資産": soshisan}

def pick_use_idx_list(num):
    if num == 0:
        llist = use_idx_profit
        open = list(llist.keys())
        result = []
        it = input(f"choose_first!: {open}")
        result.append(llist[it])
        it = input(f"choose_second!: {open}")
        result.append(llist[it])
        return int(result[0]), int(result[1])
    elif num == 1:
        llist = use_idx_safety
        open = list(llist.keys())
        result = []
        it = input(f"choose_first!: {open}")
        result.append(llist[it])
        it = input(f"choose_second!: {open}")
        result.append(llist[it])
        return int(result[0]), int(result[1])
    elif num == 2:
        llist = use_idx_product
        open = list(llist.keys())
        result = []
        it = input(f"choose_first!: {open}")
        result.append(llist[it])
        it = input(f"choose_second!: {open}")
        result.append(llist[it])
        return int(result[0]), int(result[1])
    # num == 3:nothing
    elif num == 4:
        llist = use_idx_activity
        open = list(llist.keys())
        result = []
        it = input(f"choose_first!: {open}")
        result.append(llist[it])
        it = input(f"choose_second!: {open}")
        result.append(llist[it])
        return int(result[0]), int(result[1])



# finance_classのラベルをつける{"profit": 0, "safety": 1, "product": 2, "growth": 3, "activity": 4}
# get 0 or 1 or 2 or 3 
def get_idx_in_finance_class(finance_class_name):
    idx_in_finance_class_dic = {}
    for i in range(len(finance_class_name)):
        idx_in_finance_class_dic[finance_class_name[i]] = i
    while True:
        catch_request = input(f"please choose {idx_in_finance_class_dic.keys()}?:\n")
        if catch_request in list(idx_in_finance_class_dic.keys()):
            break
        else:
            print("Error,, please One More!!")
    return idx_in_finance_class_dic[catch_request]


import copy
unnes_calc_profit = ["売上高総利益率", "売上高営業利益率"]  # profit
unnes_calc_safety = [] # safety
unnes_calc_product = [] # product
unnes_calc_growth = [] # growth
unnes_calc_activity = [] # activity
unnes_dic = {
    0: unnes_calc_profit,
    1: unnes_calc_safety,
    2: unnes_calc_product,
    3: unnes_calc_growth,
    4: unnes_calc_activity
}

# 2つ以上の指標の値を計算する必要がある指標名をリストに詰める。:need_calc_idx
# target = ["***", "***"]
def make_chance(idx_in_finance_class, num):
    need_calc_index = copy.copy(calc_impossible[idx_in_finance_class])
    for i in unnes_dic[num]:
        need_calc_index.remove(i)
    return need_calc_index
        
# ①まずインデックスを取り出す
# 収益性--------------------------------------------------------------
uriage_all_pr = columns_list.index("売上総利益率")
uriage_eigyo_pr = columns_list.index("営業利益率") # 売上高営業利益率
uriage_all_pr = columns_list[uriage_all_pr]
uriage_eigyo_pr = columns_list[uriage_eigyo_pr]
# ---------------------------------------------------------------収益性
# 安全性---------------------------------------------------------------

# ---------------------------------------------------------------安全性
# 生産性---------------------------------------------------------------

# ---------------------------------------------------------------生産性
# 成長性---------------------------------------------------------------

# ---------------------------------------------------------------成長性
# 活動性---------------------------------------------------------------

# ---------------------------------------------------------------活動性

dif_only_surface = [uriage_all_pr, uriage_eigyo_pr]

# ④③のリストの長さを変数に入れる
dif_only_surface_len = len(dif_only_surface)
chance = calc_impossible[0][:dif_only_surface_len]
    

# calc calc_impossible
def calc_calc_impossible(idx_in_finance_class):
    dd_idx_value = {}
    num = idx_in_finance_class
    need_calc_index = make_chance(idx_in_finance_class, num)
    print(need_calc_index)
    print(num)
    dif_only_surface_count = 0
    for idx_name in calc_impossible[idx_in_finance_class]:
        dd_value = []
        # need_calc_indexなら計算に使う指標を選択
        if idx_name in need_calc_index:
            first, second = pick_use_idx_list(num)
        for k in data_list:
            if idx_name in chance:  # 指標の表記が違うだけの計算
                dd_value.append(
                    k.at[2020, dif_only_surface[dif_only_surface_count]]
                )
            elif idx_name in need_calc_index:  # 2つの指標を計算して算出する指標
                next = "do"
                # 値が"-"の場合は計算できないのでスキップdd_value: "計算不可"
                if type(k.at[2020, columns_list[first]]) is str or type(k.at[2020, columns_list[second]]) is str:
                    dd_value.append("計算不可")
                    next = "skip"
                if next == "do":
                    dd_value.append(k.at[2020, columns_list[first]] / k.at[2020, columns_list[second]])
        dif_only_surface_count += 1
        dd_idx_value[idx_name] = dd_value
    return dd_idx_value
        
result_calc_impossible_profit = calc_calc_impossible(get_idx_in_finance_class(finance_class_name))
result_calc_impossible_safety = calc_calc_impossible(get_idx_in_finance_class(finance_class_name))
result_calc_impossible_product = calc_calc_impossible(get_idx_in_finance_class(finance_class_name))
result_calc_impossible_growth = calc_calc_impossible(get_idx_in_finance_class(finance_class_name))
result_calc_impossible_activity = calc_calc_impossible(get_idx_in_finance_class(finance_class_name))

result_calc_impossible = [
    result_calc_impossible_profit,
    result_calc_impossible_safety,
    result_calc_impossible_product,
    result_calc_impossible_growth,
    result_calc_impossible_activity
]


# print(unnes_calc_index)
print("~"*200)
print(result_calc_possible)
print(result_calc_impossible)
print("~"*200)
print(len(result_calc_possible))
print(len(result_calc_impossible))


merge_result = [i.update(j) for i, j in zip(result_calc_possible, result_calc_impossible)]

print(merge_result)

# result_calc_possibleを最終結果に更新
[i.update(j) for i, j in zip(result_calc_possible, result_calc_impossible)]


print(result_calc_possible)

dic1 = result_calc_possible[0]
dic2 = result_calc_possible[1]
dic3 = result_calc_possible[2]
dic4 = result_calc_possible[3]
dic5 = result_calc_possible[4]

dic_list = [dic1, dic2, dic3, dic4, dic5]
all_dic = {}

for i in dic_list:
    all_dic.update(i)
    
print(all_dic)
print(len(all_dic))

idx = [
    "cyberagent",
    "fujitsu",
    "hitachi",
    "kddi",
    "ntt",
    "panasonic",
    "rakuten",
    "softbank",
    "sony"
]

df_finance = pd.DataFrame(
    data = all_dic, index=idx
)

print(df_finance.head())
print(df_finance.shape)

df_finance.to_csv("finance_data.csv", encoding="shift jis")