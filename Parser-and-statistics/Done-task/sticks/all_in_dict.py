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
    min_price = 10 ** 100
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
    most_common_region = []
    for wine in wine_data:
        if wine['designation'] != name:
            continue
        if wine['region_1'] is None:
            continue
        else:
            counter_wine += 1
            counter[wine['region_1']] += 1

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
    most_common_country = []
    for wine in wine_data:
        if wine['designation'] != name:
            continue
        if wine['country'] is None:
            continue
        else:
            counter_wine += 1
            counter[wine['country']] += 1

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


def most_expensive_wine(data):
    max_price = 0
    titles = []
    for wine in wine_data:
        if wine['designation'] is None or wine['price'] is None:
            continue
        if wine['price'] > max_price:
            max_price = wine['price']
            titles.clear()
            titles.append(wine['designation'])
        elif wine['price'] == max_price:
            titles.append(wine['designation'])
    return titles


def cheapest_wine(data):
    min_price = 10 ** 1000
    titles = []
    for wine in wine_data:
        if wine['designation'] is None:
            continue
        if wine['price'] is None:
            continue
        if wine['price'] < min_price:
            min_price = wine['price']
            titles.append(wine['designation'])
    return titles


def highest_score(data):
    titles = []
    max_points = 0
    for wine in wine_data:
        if wine['designation'] is None:
            continue
        if wine['points'] is None:
            continue
        if int(wine['points']) > max_points:
            max_points = int(wine['points'])
            titles.clear()
            titles.append(wine['designation'])
        elif int(wine['points']) == max_points:
            titles.append(wine['designation'])
    return titles


def lowest_score(data):
    titles = []
    min_points = 10 ** 1000
    for wine in wine_data:
        if wine['designation'] is None:
            continue
        if wine['points'] is None:
            continue
        if int(wine['points']) < min_points:
            min_points = int(wine['points'])
            titles.clear()
            titles.append(wine['designation'])
        elif int(wine['points']) == min_points:
            titles.append(wine['designation'])
    return titles


def most_expensive_coutry(data):
    all_country = set()
    max_price = 0
    max_country_price = []
    for wine in wine_data:
        if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
            continue
        all_country.add(wine['country'])

    for wine_country in all_country:
        for wine in wine_data:
            if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
                continue
            if wine_country == wine['country']:
                if wine['price'] > max_price:
                    max_price = wine['price']
        max_country_price.append(max_price)
        max_price = 0

    for price in max_country_price:
        max_price += price

    return max_price / len(max_country_price)


def cheapest_country(data):
    all_country = set()
    min_price = 10 ** 1000
    min_country_price = []
    for wine in wine_data:
        if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
            continue
        all_country.add(wine['country'])

    for wine_country in all_country:
        for wine in wine_data:
            if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
                continue
            if wine_country == wine['country']:
                if wine['price'] < min_price:
                    min_price = wine['price']
        min_country_price.append(min_price)
        min_price = 10 ** 1000

    min_price = 0
    for price in min_country_price:
        min_price += price

    return min_price / len(min_country_price)


def most_rated_country(data):
    all_country = set()
    country_points = 0
    max_country_points = 0
    most_rated_country = []
    for wine in wine_data:
        if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
            continue
        all_country.add(wine['country'])

    for wine_country in all_country:
        for wine in wine_data:
            if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
                continue
            if wine_country == wine['country']:
                country_points += int(wine['points'])

        if country_points > max_country_points:
            max_country_points = country_points
            most_rated_country.clear()
            most_rated_country.append(wine_country)

        elif country_points == max_country_points:
            most_rated_country.append(wine_country)

        country_points = 0

    return most_rated_country


def underrated_country(data):
    all_country = set()
    country_points = 0
    min_country_points = 10 ** 1000
    most_underated_country = []
    for wine in wine_data:
        if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
            continue
        all_country.add(wine['country'])

    for wine_country in all_country:
        for wine in wine_data:
            if wine['designation'] is None or wine['price'] is None or wine['country'] is None:
                continue
            if wine_country == wine['country']:
                country_points += int(wine['points'])

        if country_points < min_country_points:
            min_country_points = country_points
            most_underated_country.clear()
            most_underated_country.append(wine_country)

        elif country_points == min_country_points:
            most_underated_country.append(wine_country)

        country_points = 0

    return most_underated_country


stat = {
    'statistics': {},
    'most_expensive_wine': {},
    'cheapest_wine': {},
    'highest_score': {},
    'lowest_score': {},
    'most_expensive_coutry': {},
    'cheapest_country': {},
    'most_rated_country': {},
    'underrated_country': {}

}


wines = {}
for wine in ('Gew[üu]rztraminer', 'Riesling', 'Merlot', 'Madera', 'Tempranillo', 'Red Blend'):
    wine_name_stat = {
        'avarege_price': avarege_price(wine),
        'min_price': min_price(wine),
        'max_price': max_price(wine),
        'most_common_region': most_common_region(wine),
        'most_common_country': most_common_country(wine),
        'avarage_score': avarage_score(wine)
    }
    wines[wine] = wine_name_stat

stat['statistics']['wine'] = wines
stat['statistics']['wine'] = wines
stat['most_expensive_wine'] = most_expensive_wine(wine_data)
stat['cheapest_wine'] = cheapest_wine(wine_data)
stat['highest_score'] = highest_score(wine_data)
stat['lowest_score'] = lowest_score(wine_data)
stat['most_expensive_coutry'] = most_expensive_coutry(wine_data)
stat['cheapest_country'] = cheapest_country(wine_data)
stat['most_rated_country'] = most_rated_country(wine_data)
stat['underrated_country'] = underrated_country(wine_data)

pprint(stat)
