import requests
import json
import urllib
from bs4 import BeautifulSoup

BASE_URL = 'http://data-interview.enigmalabs.org/companies'


def fetch_company_names(page_number):
    if page_number > 1:
        payload = urllib.urlencode({'page': str(page_number)})
        full_url = BASE_URL + '?' + payload
        r = requests.get(full_url)
    else:
        r = requests.get(BASE_URL)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    urls = list()
    for element in soup.findAll('a', id=True):
        urls.append(element['href'])
    return urls


def fetch_company_page(url_path):
    full_url = BASE_URL + url_path
    r = requests.get(full_url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    return soup


def make_url(company_url):
    company_encoded = company_url.replace(' ', '%20')
    company = company_encoded[company_encoded.rfind('/'):]
    return company


if __name__ == '__main__':
    fields = None
    company_info_list = list()
    for i in range(1, 11):
        companies = fetch_company_names(i)
        url_encoded_companies = map(make_url, companies)
        soups = map(fetch_company_page, url_encoded_companies)
        if fields is None:  # run it once for efficency
            fields = map(lambda x: x.get_text(), soups[0].findAll('b'))
        all_company_info = map(lambda x: x.findAll('td', id=True), soups)
        for company_info in all_company_info:
            company_fields = map(lambda x: x.get_text(), company_info)
            company = dict(zip(fields, company_fields))
            company_info_list.append(company)
    with open('solution.json', 'w') as outfile:
        json.dump(company_info_list, outfile)
