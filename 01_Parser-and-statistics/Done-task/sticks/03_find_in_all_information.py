# Найти:
#
# most_expensive_wine в случае коллизий тут и далее делаем список.
# cheapest_wine
# highest_score
# lowest_score
# most_expensive_coutry в среднем цена на самое дорогое вино среди стран
# cheapest_coutry в среднем цена на самое дешевое вино среди стран
# most_rated_country
# underrated_country

import json


with open('winedata_full.json', 'r') as json.file:
    wine_data = json.load(json.file)


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

    return max_price / len(max_country_price), max_country_price


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
    min_country_points = 10**1000
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

