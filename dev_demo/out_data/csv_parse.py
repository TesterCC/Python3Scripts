import csv
import json

json_file = "./data/11.json"
with open(json_file, 'r', encoding='utf-8') as f:
    out_dict = json.load(f)

print(type(out_dict), len(out_dict))  # 155
print(out_dict[0])
print(out_dict[0].keys())
# print(out_dict)
print("-" * 66)

# for odict in out_dict:
#     print(odict['cve_number'])
for i in out_dict:
    if i['cve_number'] == 'CVE-2014-2928':
        print(i)

print("===debug=================")

db_cve = [i['cve_number'] for i in out_dict]
db_name = [i['name'] for i in out_dict]  # 155

# print(f"len1:{len(db_cve)}")
#
# db_cve = list(set(db_cve))   # no repeat
#
# print(f"len2:{len(db_cve)}")

print("=" * 66)
import_cve = ['CVE-2023-21608',
              'CVE-2023-21839',
              'CVE-2023-0669',
              'CVE-2023-23752',
              'CVE-2023-25136',
              'CVE-2023-22974',
              'CVE-2023-22809',
              'CVE-2023-0297',
              'CVE-2023-0179',
              'CVE-2023-22855',
              'CVE-2022-25237',
              'CVE-2022-36446',
              'CVE-2022-36804',
              'CVE-2022-2992',
              'CVE-2022-26134',
              'CVE-2022-42889',
              'CVE-2022-34265',
              'CVE-2022-32532',
              'CVE-2022-22980',
              'CVE-2022-33980',
              'CVE-2022-37661',
              'CVE-2022-22978',
              'CVE-2022-27925',
              'CVE-2022-0540',
              'CVE-2022-1329',
              'CVE-2022-24706',
              'CVE-2022-29464',
              'CVE-2022-22965',
              'CVE-2022-22947',
              '1Day',
              '1Day',
              '1Day',
              '1Day',
              'CVE-2016-1287',
              'CVE-2020-3187',
              'CVE-2018-0101',
              'CVE-2018-0296',
              'CVE-2020-3452',
              'CVE-2016-6366',
              'CVE-2016-6367',
              '0Day',
              'CVE-2021-1167',
              'CVE-2020-3332',
              'CVE-2021-1520',
              'CVE-2019-1663',
              'CVE-2020-3330',
              'CVE-2020-3331',
              'CVE-2021-1414',
              'CVE-2021-1472',
              'CVE-2022-20707',
              'CVE-2022-20699',
              'CVE-2021-34730',
              '1day',
              'CVE-2017-6736',
              'CVE-2017-3881',
              'CVE-2018-0171',
              'CVE-2019-19781',
              'CVE-2020-8195_8196',
              'CVE-2020-8193',
              'CVE-2020-8198',
              '0Day',
              '0Day',
              '1Day',
              'CVE-2019-17621',
              'CVE-2016-9244',
              'CVE-2015-5477',
              'CVE-2020-5902',
              'CVE-2021-22986',
              'CVE-2014-2928',
              'CVE-2022-41622',
              'CVE-2022-41800',
              'CVE-2022-1388',
              'CVE-2015-4040',
              'CVE-2015-3628',
              '0Day',
              '1Day',
              '0Day',
              'CVE-2018-13374',
              'CVE-2018-13382',
              'CVE-2020-12812',
              'CVE-2018-13381',
              '1Day',
              '1Day',
              'CVE-2018-13379',
              'CVE-2016-1909',
              'CVE-2022-40684',
              'CVE-2018-13383',
              'CVE-2017-17215',
              'CVE-2021-0204',
              'CVE-2021-0255',
              'CVE-2021-0256',
              'CVE-2021-0218',
              'CVE-2021-0219',
              'CVE-2021-0223',
              'CVE-2019-11510',
              'CVE-2019-11539',
              'CVE-2020-8243',
              'CVE-2020-8260',
              'CVE-2021-22900',
              'CVE-2021-22937',
              'CVE-2020-8255',
              'CVE-2020-1631',
              '1Day',
              'CVE-2021-0210',
              'CVE-2022-22245',
              '0day',
              'CVE-2015-7756',
              'CVE-2015-7755',
              'CVE-2018-7445',
              '1Day',
              'CVE-2017-7285',
              'CVE-2017-17538',
              'CVE-2017-6444',
              'CVE-2018-10070',
              'CVE-2018-14847',
              '0Day',
              '0Day',
              '0Day',
              'CVE-2019-17137',
              'CVE-2019-17372',
              'CVE-2020-27866',
              'CVE-2021-45511',
              'CVE-2020-17409',
              'CVE-2021-35973',
              'CVE-2021-41383',
              'CVE-2020-10929',
              'CVE-2020-35220',
              'CVE-2021-44261',
              'CVE-2020-10923-24',
              'CVE-2020-15416',
              'CVE-2020-27867',
              'CVE-2021-31802',
              'CVE-2020-26919',
              'CVE-2019-20760',
              'CVE-2020-2039',
              'CVE-2017-15944',
              'CVE-2019-1579',
              'CVE-2020-2037',
              'CVE-2020-2038',
              'CVE-2019-16667',
              'CVE-2014-4688',
              'CVE-2019-12949',
              'CVE-2019-16701',
              'CVE-2019-12585',
              'CVE-2021-41282',
              'CVE-2022-31814',
              'CVE-2014-6247',
              'CVE-2021-20038',
              '1Day',
              'CVE-2021-20045',
              'CVE-2016-9682',
              'CVE-2016-9683',
              'CVE-2016-9684',
              '1Day',
              '0Day',
              'CVE-2021-20039',
              'CVE-2021-20044',
              'CVE-2019-7481',
              'CVE-2021-20034',
              'CVE-2020-15504',
              '1Day',
              'CVE-2022-1040',
              'CVE-2022-3236',
              'CVE-2018-16116',
              'CVE-2018-16117',
              '1Day',
              'CVE-2017-12854',
              'CVE-2020-11698',
              'CVE-2020-11699',
              'CVE-2020-11700',
              'CVE-2020-11803',
              'CVE-2020-11804',
              'CVE-2020-24046',
              'CVE-2020-10987',
              '1Day',
              'CVE-2016-7089',
              'CVE-2019-12725',
              'CVE-2020-29390',
              'CVE-2020-29583']

# 在db_cve，不在import_cve
print(f"[D] total db cves: {len(db_cve)}")

repeat_cve = []
no_repeat_cve = []

for j in db_cve:
    if j not in ["0Day", "1Day"]:
        if j in import_cve:
            repeat_cve.append(j)
        else:
            no_repeat_cve.append(j)

print(f"[D] repeat: {len(repeat_cve)}")

print(f"[D] no repeat: {len(no_repeat_cve)}")
print(no_repeat_cve)
