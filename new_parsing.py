'''Импортируем модуль Requests, чтобы собрать данные с веб-страницы.
Библиотека Beautiful Soup создает дерево синтаксического разбора и сделает текст веб-страницы,
извлеченный с помощью Requests, более удобочитаемым.'''
import requests
from bs4 import BeautifulSoup

'''Функция принимает на входе url обрабатывается модулем request и на выходе
возвращает  текстовое содержимае веб страницы'''

def get_html(url):
    page = requests.get(url)
    return page.text

'''Функция определения количества страниц книги. Принимает на входе текстовое содержимое веб страницы,
 затем получает обьект Soup через встроеный парсер.Находим id секцию содержащую теги с ссылками и получаем последнюю ссылку.
 Сплитим сылку и забираем число  которое было после =. Возвращаем число переводя его из str в int'''

def get_total_pages(get_html):
    soup = BeautifulSoup(get_html, 'lxml')
    pages = soup.find('div', id="div_paginator").find_all('a')[-1].get('href')
    total_pages = pages.split('=')[2]
    return int(total_pages)

''' Функция получения низвания книги.Передаем текстовое содержимое страницы затем получаем обьект soup.
В нем исчем секцию id с текстом и в нем есчем и забираем название.Фарматируем  строку с названием добавляя расширени .txt.
  Возвращем название книги в формате "Name.txt".'''

def get_name(get_html):
    soup = BeautifulSoup(get_html, 'lxml')
    book = soup.find('div', id='ptext').find_all('p')[1].text
    name_book = "{}.txt".format(book)
    return name_book

'''Основная функция. Получает через ввод url, содержит макет построения ссылки,
 через цикл for  генерирует url исходя из общего количества страниц, получает её обробатывает парсером,
  делает поиски по секциям id, для поиска текста.Затем создает фаил и по строчно записывает в него текст.'''

def main():
    url = input('Enter the URL: ')
    base_url = url
    page_part = '&page='
    total_pages =  get_total_pages(get_html(base_url))
    for i in range(0, total_pages):
        url_gen = base_url + page_part + str(i+1)
        page = requests.get(url_gen)
        soup = BeautifulSoup(page.text, 'lxml')
        text = soup.find('div', id='ptext').find_all('p')
        count = len(text)
        for i in range(1, count):
            text_book = text[i].text
            filename = open(get_name(get_html(url)), 'a')
            filename.write(text[i].text + '\n')
            filename.close()
            print(text_book)


if __name__ == '__main__':
    main()