import json


titles = set()
wines_unique = []


def parser(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        for record in data:
            if record['title'] in titles:
                continue
            titles.add(record['title'])
            wines_unique.append(record)


parser("winedata_1.json")
parser("winedata_2.json")


def key_sort(x):
    f1 = x['price']
    if f1 is None:
        f1=0
    f2 = x['designation']
    if f2 is None:
        f2 = ""
    return f1, f2


wines_unique.sort(key=key_sort)

with open('winedata_full.json', 'w') as outfile:
    json.dump(wines_unique, outfile)
