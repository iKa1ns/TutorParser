import requests
from bs4 import BeautifulSoup as bs

url = 'https://pythontutor.ru/lessons/inout_and_arithmetic_operations/'


def get_html(url: str) -> str:
    """
    Функция для отправки запроса
    :param url:
    :return:
    """

    html = requests.get(url)
    return html.text


def get_section() -> list[str]:
    """
    Функция для вычленения названий задач
    :return:
    """

    arr_title = []
    soup = bs(get_html(url), 'html.parser')
    item_title = soup.findAll(class_="lesson__item_title")
    c = 0

    for i in item_title:
        c += 1
        arr_title.append(str(c) + ' ' + i.text)

    return arr_title


print('\n'.join(get_section()))
index = int(input('Выберите раздел: ')) - 1
print('\n')

def get_url(index):
    arr_url = []
    soup = bs(get_html(url), 'html.parser')
    url_get = soup.find_all(class_="lesson")

    for i in url_get:
        arr_url.append(i.find('a').get('href'))

    new_url = 'https://pythontutor.ru' + arr_url[index]
    return new_url


def get_tasks():
    new_html = requests.get(get_url(index))
    new_soup = bs(new_html.text, 'html.parser')

    for i in (new_soup.find_all(class_="problems_link")):
        return i.text.strip().split('\n')[2:]


print('\n'.join(get_tasks()))
