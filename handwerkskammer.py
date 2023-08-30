import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


main_list = []

def extract(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup.find_all('div', class_ = 'searchhit-result')


def transform(articles):

    for item in articles:
        name = item.find('h2', class_ = 'h4').text
        address_tag = item.find('div', class_='searchhit-text').address
        adress = ' '.join(address_tag.stripped_strings)
    
        business = {
            'name' : name,
            'adress' : adress
        }

        main_list.append(business)
    return

def load():
    df = pd.DataFrame(main_list)
    df.to_csv('DachdeckerHildesheimm.csv', index=False, encoding='ISO-8859-1')

#need to define how many pages of the webpage should be scrapped, in stepts by ten
for x in [0, 10, 20]:
    print(f'seite {x}')
    articles = extract(f'https://www.hwk-hildesheim.de/betriebe/suche-24,0,bdbsearch.html?limit=10&search-searchterm=&search-job=Dachdecker&search-local=0&search-filter-zipcode=31134&search-filter-latitude=52.145556&search-filter-latitude=52.145556&search-filter-latitude=52.145556&search-filter-latitude=52.145556&search-filter-latitude=52.145556&search-filter-latitude=52.145556&search-filter-longitude=9.953611&search-filter-longitude=9.953611&search-filter-longitude=9.953611&search-filter-longitude=9.953611&search-filter-longitude=9.953611&search-filter-longitude=9.953611&search-filter-radius=20&search-filter-jobnr=11040&search-filter-training=&search-filter-experience=&offset={x}')
    transform(articles)
    time.sleep(5)


load()
print('csv gespeichert')
