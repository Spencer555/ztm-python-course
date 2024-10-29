# scrapping - downloading a data from webpage cleaning it up and using it

# websites tell us what we are allowed and not allowed to do in the robots.txt

# check the robots.txt before u scrape

import requests
from bs4 import BeautifulSoup
import pprint  # make the printing prettier


res = requests.get('https://news.ycombinator.com/')
res_1 = requests.get('https://news.ycombinator.com/?p=2')


# parsing the data so it become an obj we can manipulate
# this creates what we call a soup object
soup = BeautifulSoup(res.text, 'html.parser')
soup_1 = BeautifulSoup(res_1.text, 'html.parser')
hn_links = soup.select('.titleline')
hn_subtext = soup.select('.subtext')
hn_1_links = soup_1.select('.titleline')
hn_1_subtext = soup_1.select('.subtext')


mega_links = hn_links + hn_1_links
mega_subtext = hn_subtext  + hn_1_subtext
# class is  . id is #
# print(soup.select('.score'))


def create_custom_hn(links, subtext):
    hn = []
    # we only want to add the text from links and not the html

    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].select('a')[0].get('href', None)
        vote = subtext[idx].select('.score')
        # import pdb
        # pdb.set_trace()
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 1:

                hn.append({
                    'title':title,
                    'link':href,
                    'votes': points
                })

    # sorting by votes in decending order

    hn.sort(key=lambda x: x['votes'], reverse=True)
    # hn.sort(key=lambda x: -x['votes'])
    return hn


print(create_custom_hn(mega_links, mega_subtext))