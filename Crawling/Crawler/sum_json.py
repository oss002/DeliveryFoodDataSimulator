import json

with open("./Data.json", 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

with open("./Data_ajou_분식_6.json", 'r', encoding='utf-8') as f:
    add_data = json.load(f)

print(add_data)

add_store_num = len(json_data['store'])
add_menu_num = len(json_data['menu'])

check_store_name = []

for k in json_data['store']:
    check_store_name.append(k["s_name"])

check_store_id = []

sub_s_cnt = 0

for i in add_data['store']:
    if i["s_name"] in check_store_name:
        check_store_id.append(i["s_id"])
        sub_s_cnt += 1
    else:
        i["s_id"] += add_store_num
        i["s_id"] -= sub_s_cnt
        json_data['store'].append(i)

sub_m_cnt = 0
sub_ms_cnt = 0

prev_ms = -1
for j in add_data['menu']:
    if not (j["ms_id"] in check_store_id):
        j["ms_id"] += add_store_num
        j["ms_id"] -= sub_ms_cnt
        j["m_id"] += add_menu_num
        j["m_id"] -= sub_m_cnt
        json_data['menu'].append(j)

    else:
        sub_m_cnt += 1
        if not (prev_ms == j["ms_id"]):
            sub_ms_cnt += 1
        prev_ms = j["ms_id"]

with open("./Data.json", 'w', encoding='utf-8') as outfile:
    json.dump(json_data, outfile, ensure_ascii=False, indent='\t')

print('end')

## 첫 파일 만들기 with ca data
# json_data = {'store':[], 'menu':[]}
#
# with open("./Data_ca.json", 'r', encoding='utf-8') as f:
#     add_data = json.load(f)
#
# print(add_data)
#
# add_store_num = len(json_data['store'])
# add_menu_num = len(json_data['menu'])
#
# #
# # check_store = []
# # for k in json_data['store'] :
# #     check_store.append({ sname: k["s_name"], k["s_id"]})
#
# for i in add_data['store']:
#     json_data['store'].append(i)
#
# for j in add_data['menu']:
#     json_data['menu'].append(j)
#
# with open("./Data.json", 'w', encoding='utf-8') as outfile:
#     json.dump(json_data, outfile, ensure_ascii=False, indent='\t')
#
# print('end')
#

## 오류 잡기
# import json
#
# with open("./Data.json", 'r', encoding='utf-8') as json_file:
#     json_data = json.load(json_file)
#
# for i in json_data["menu"]:
#     if i["ms_id"] >= 1972:
#         i["ms_id"] -= 1
#
# with open("./Data.json", 'w', encoding='utf-8') as outfile:
#      json.dump(json_data, outfile, ensure_ascii=False, indent='\t')
