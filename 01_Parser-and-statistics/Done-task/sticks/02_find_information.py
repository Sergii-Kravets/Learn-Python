#Найти для сортов Gew[üu]rztraminer, Riesling, Merlot, Madera, Tempranillo, Red Blend следующую информацию:
#
#avarege_price
#min_price
#max_price
#most_common_region где больше всего вин этого сорта производят ?
#most_common_country
#avarage_score


import json
from pprint import pprint


with open('winedata_full.json', 'r') as json.file:
    wine_data = json.load(json.file)


def avarege_price(name):
    total = 0
    counter = 0
    for wine in wine_data:
        if wine['designation'] == name:
            if wine['price'] is None:
                continue
            counter += 1
            total += wine['price']
    if counter == 0:
        return ('There is no such wine as', name)
    return total / counter

def min_price(name):
    min_price = 10**100
    counter = 0
    for wine in wine_data:
        if wine['designation'] == name:
            counter += 1
            if wine['price'] is None:
                continue
            if wine['price'] < min_price:
                min_price = wine['price']
    if counter == 0:
        return ('There is no such wine as', name)
    return min_price

def max_price(name):
    counter = 0
    max_price = 0
    for wine in wine_data:
        if wine['designation'] == name:
            counter += 1
            if wine['price'] is None:
                continue
            if wine['price'] > max_price:
                max_price = wine['price']
    if counter == 0:
        return ('There is no such wine as', name)
    return max_price

def most_common_region(name):
    from collections import Counter
    counter_wine = 0
    counter = Counter()
    most_common_region =[]
    for wine in wine_data:
        if wine['designation'] != name:
            continue
        if wine['region_1'] is None:
            continue
        else:
            counter_wine += 1
            counter[wine['region_1']]+=1

    if counter_wine == 0:
        return ('There is no such wine as', name)

    most_occur = counter.most_common()

    if len(most_occur) == 1:
        return [most_occur[0][0]]

    for element_wine in range(len(most_occur) - 1):
        if most_occur[0][1] == most_occur[element_wine][1]:
            most_common_region.append(most_occur[element_wine][0])

    return most_common_region

def most_common_country(name):
    from collections import Counter
    counter_wine = 0
    counter = Counter()
    most_common_country =[]
    for wine in wine_data:
        if wine['designation'] != name:
            continue
        if wine['country'] is None:
            continue
        else:
            counter_wine += 1
            counter[wine['country']]+=1

    if counter_wine == 0:
        return ('There is no such wine as', name)

    most_occur = counter.most_common()

    if len(most_occur) == 1:
        return [most_occur[0][0]]

    for element_wine in range(len(most_occur) - 1):
        if most_occur[0][1] == most_occur[element_wine][1]:
            most_common_country.append(most_occur[element_wine][0])

    return most_common_country

def avarage_score(name):
    total_points = 0
    counter = 0
    for wine in wine_data:
        if wine['designation'] == name:
            if wine['points'] is None:
                continue
            counter += 1
            total_points += int(wine['points'])
    if counter == 0:
        return ('There is no such wine as', name)
    return total_points / counter



for wine in ('Gew[üu]rztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend'):
    print(most_common_country(wine))
