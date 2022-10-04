import requests
from bs4 import BeautifulSoup
import pprint
import time


res = requests.get('https://news.ycombinator.com/')
p = 1

def request_pages(p):
    if p == 1:
        res = requests.get('https://news.ycombinator.com/')
    else:
        res = requests.get('https://news.ycombinator.com/news?p=' + str(p))

    return res.text

while p <= 10:
    time.sleep(5)
    res = requests.get('https://news.ycombinator.com/news?p=' + str(p))
    soupQ = BeautifulSoup(request_pages(p), 'html.parser')
    linksQ = (soupQ.select('.titleline'))
    subtextQ = (soupQ.select('.subtext'))
    if p == 1:
        linksVar = linksQ
        subtextVar = subtextQ
    else:
        linksVar = linksQ + links
        subtextVar = subtextQ + subtextVar
    links = linksVar
    subtext = subtextVar
    p +=1
    print(p)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse = True)

def create_custom_hackerNews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title =item.getText()
        href = item.find('a').get('href', None) #* item is the same as links[idx]
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hackerNews(links, subtext))

