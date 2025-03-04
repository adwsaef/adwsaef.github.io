import requests
import sys
from bs4 import BeautifulSoup
import string
import re

def set_output(fname, type):
    f = open(fname, type)
    sys.stdout = f

def get_sufix(text):
    at_index = text.index("@")
    return text[at_index + 1:]

def init_page(title):
    print('---')
    print('layout: default')
    print('---')

adress = "https://www.favikon.com/blog/top-10-most-followed-tiktok-influencers"

response = requests.get(adress)
    
soup = BeautifulSoup(response.text, 'html.parser')

main_page = 'index.markdown'

#set_output(main_page,'w')
#init_page('10 famous tiktokers')


i = 1
for link in soup.find_all('a'):
    url_link = link.get('href')
    if 'www.tiktok.com' in url_link:
        name = get_sufix(url_link)
        sub_page = name + '.html'
        print('### ' + str(i) + '. [' + name + '](' + './' + sub_page + ')')
        set_output(sub_page,'w')
        init_page('')
        print('<h1>' + name + '</h1>')
        print('<br>')
        print('Creator tiktok: ' +  '<a href="' + url_link + '">' + url_link + '</a>')
        print('<br>')
        for paragraph in soup.find_all("p"):
            text = paragraph.get_text(strip=True)  # Remove extra whitespace
            if (text[:3].lower() == name[:3].lower()):
                print('<br>')
                print('<h3>')
                print(text)
                print('</h3>')
                print("\n")  # Separate paragraphs with a newline

        for img in soup.find_all("img"):
            photo_link = img["src"]
            if (text[:3].lower() in photo_link):
                print(img["src"])

        set_output(main_page,'a')
        i = i + 1