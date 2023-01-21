import concurrent
import datetime
import requests
import pytz


def get_country(name: str):
    NATIONALIZE_URL = "https://api.nationalize.io"
    response = requests.get(NATIONALIZE_URL, params={'name': name})
    if response.status_code < 400:
        country_dict = response.json()
        country_id = country_dict['country'][0]['country_id']
        return country_id
    else:
        raise Exception(f"there is an error: {response.status_code}")


def get_country_name(country_id):
    INFO_URL = "https://restcountries.com/v3.1/alpha/"
    COUNTRY_URL = INFO_URL + country_id
    response = requests.get(COUNTRY_URL)
    if response.status_code < 400:
        response_dict = response.json()
        return response_dict[0]["name"]["common"]
    else:
        raise Exception('bad response from INFO_URL')


def get_continent(country_id):
    INFO_URL = "https://restcountries.com/v3.1/alpha/"
    COUNTRY_URL = INFO_URL + country_id
    response = requests.get(COUNTRY_URL)
    if response.status_code < 400:
        response_dict = response.json()
        return response_dict[0]['continents']
    else:
        raise Exception('bad response from INFO_URL')


def get_language(country_id):
    INFO_URL = "https://restcountries.com/v3.1/alpha/"
    COUNTRY_URL = INFO_URL + country_id
    response = requests.get(COUNTRY_URL)
    if response.status_code < 400:
        response_dict = response.json()
        return response_dict[0]["languages"]
    else:
        raise Exception('bad response from INFO_URL')


def get_country_time():
    tz = pytz.timezone(country_name)
    current_time = datetime.datetime.now(tz)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


if __name__ == '__main__':
    names = input("please enter your name(comma separated) :")
    names = names.split(',')
    country_id = get_country(names)
    country_name = get_country_name(country_id)
    with concurrent.futures.ThreadPoolExecutor as executer:
        executer.map(get_country, names)

    print(f"your name is:{names.capitalize()}\nyour most likely country to have your name is {country_name}\n")
