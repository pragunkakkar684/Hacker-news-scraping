import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select('.titleline a')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(link, subtext):
    hn = []
    for idx, item in enumerate(link):
        title = link[idx].getText()
        href = link[idx].get('href', None)
        if idx < len(subtext):
            votes = subtext[idx].select('.score')
            if votes:
                points = int(votes[0].getText().replace(' points', ''))
                if points>99:
                    hn.append({'title': title, 'link': href, 'votes': points})
            else:
                print(f'No votes for {title}')
    return sort_stories_by_votes(hn)

for story in create_custom_hn(links, subtext):
    pprint.pprint(story)
