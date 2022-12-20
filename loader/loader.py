import random
import bs4
import requests

API_KEY = '9f1134e3-3878-4263-80db-76170259c3b0'

USER_AGENTS_LIST = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]


def fetch(url, identifier):
    return get_data(get_content(get_soup(get_request(url)), identifier))


def get_content(soup, *args):
    return soup.find_all(*args)


def get_request(url):
    try:
        return requests.get(url=url,
                            headers={
                                'api_key': API_KEY,
                                'User-Agent': random.choice(USER_AGENTS_LIST)}
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
