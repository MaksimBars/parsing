import requests
from bs4 import BeautifulSoup
base_url = 'http://book-online.com.ua/read.php?book=1&page='
for i in range(1, 230):
    page = requests.get(base_url + str(i))
    soup = BeautifulSoup(page.text, 'html.parser')
    t = soup.find('div', id='ptext').find_all('p')
    count = len(t)
    filename = 'book.txt'
    for i in range(1, count):
        book = t[i].text
        filename = open('book.txt','a')
        filename.write(t[i].text + '\n')
        filename.close()
        print(book)
