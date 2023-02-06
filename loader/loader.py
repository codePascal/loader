import os.path
import random
import bs4
import requests

import loader.io as io

CONFIG_PATH = os.path.join(os.path.dirname(__file__))


def fetch(url, identifier):
    return get_data(get_content(get_soup(get_request(url)), identifier))


def get_content(soup, *args):
    return soup.find_all(*args)


def get_request(url):
    try:
        return requests.get(url=url,
                            headers={
                                'api_key': get_api_key(),
                                'User-Agent': get_rand_user_agent()}
                            )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_row_data(tr, tag='td'):
    return [td.get_text(strip=True) for td in tr.find_all(tag)]


def get_soup(request, parser="html.parser"):
    return bs4.BeautifulSoup(request.content, parser)


def get_data(content):
    if isinstance(content, list):
        data = list()
        for i in range(len(content)):
            data.append(get_table_data(content[i]))
        return data
    else:
        return get_table_data(content)


def get_table_data(table):
    data = list()
    rows = table.find_all('tr')
    header = 0
    for j, row in enumerate(rows):
        if get_row_data(row, 'th'):
            data.append(get_row_data(row, 'th'))
            header = j
    for row in rows[header + 1:]:
        data.append(get_row_data(row))
    return data


def get_api_key():
    return io.load_json(os.path.join(CONFIG_PATH, "api_key.json"))["api_key"]


def get_rand_user_agent():
    return random.choice(io.load_json(os.path.join(CONFIG_PATH, "user_agents.json"))["user_agents"])

