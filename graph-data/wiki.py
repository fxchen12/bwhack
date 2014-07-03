from bs4 import BeautifulSoup
import bs4
import urllib2
import time
import re

home_url = "http://en.wikipedia.org/wiki/"
random_uri = 'Special:Random'

def get_url(title):
    return home_url + title

def get_random_url():
    #return home_url + '2009_UEFA_European_Under-19_Championship_squads'
    return home_url + random_uri

def is_valid_href(href):
    if ':' in href:
        return False
    if href[:len('/wiki/')] != '/wiki/':
        return False        
    return True

def process_paragraph(soup):
    contents = soup.contents
    in_parenthetical = False
    for content in contents:
        if type(content) is bs4.element.NavigableString:
            if '(' in content and not in_parenthetical:
                in_parenthetical = True
            if ')' in content and in_parenthetical:
                in_parenthetical = False
        else:
            if not in_parenthetical:
                if content.name == 'a':
                    href = content.get('href')
                    if is_valid_href(href):
                        return href[len('/wiki/'):]



def get_first_link(title):
    url = get_url(title)
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)
    title = soup.title.string

    for tag in soup.find_all('table'):
        tag.replaceWith('')

    for paragraph in soup.find_all('p'):
        first_link = process_paragraph(paragraph)
        if first_link is not None:
            return first_link

    if soup.li.a is not None:
        links = soup.li.find_all('a')
        for link in links:
            href = link.get('href')
            if is_valid_href(href):
                return href[len('/wiki/'):]

    return None

def iterate(link):
    links = set()
    while link is not None and link not in links:
        print link
        links.add(link)
        link = get_first_link(link)
    print link

def main():
    iterate(random_uri)

if __name__ == "__main__":
    main()
