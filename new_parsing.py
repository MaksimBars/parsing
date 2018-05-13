"""Import the Requests module to collect data from a web page. The Beautiful Soup library creates
 a parsing tree and makes the text of the web page retrieved using Requests more readable."""
import requests
from bs4 import BeautifulSoup


def get_html(url):
    """The function accepts the url at the input is processed by request module and returns
    the text content of the web page at the output"""
    page = requests.get(url)
    return page.text


def get_total_pages(get_html):
    """Function of determining the number of pages of the book.
    Accepts the text content of the web page at the input, then receives the Soup object through the built-in parser.
    Find the section id containing the tags of the links and get latest link.
    Do split exile and take away the number which was after =. Return the number by converting it from str to int"""
    soup = BeautifulSoup(get_html, 'lxml')
    pages = soup.find('div', id="div_paginator").find_all('a')[-1].get('href')
    total_pages = pages.split('=')[2]
    return int(total_pages)


def get_name(get_html):
    """Function to obtain the title of the book.Pass the text content of the page then get the soup object.
    In it we look for the id section with the text and in it we look for and take away the name.
    Formatted string with title adding extended .txt. Return the book name in the format " Name.txt"."""
    soup = BeautifulSoup(get_html, 'lxml')
    book = soup.find('div', id='ptext').find_all('p')[1].text
    name_book = "{}.txt".format(book)
    return name_book


def main():
    """Main function. Receive, through the input url contains a layout of building links, through the loop generates
    a url based on the total number of pages, it gets processed by the parser, making the search for the sections id
    to search for text.Then creates the file and writes the text line by line"""
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