# scrapping - downloading a data from webpage cleaning it up and using it

# websites tell us what we are allowed and not allowed to do in the robots.txt

# check the robots.txt before u scrape

import requests 
from bs4 import BeautifulSoup 


res = requests.get('https://news.ycombinator.com/')


# parsing the data so it become an obj we can manipulate
# this creates what we call a soup object
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')


# print(votes[0])
# print(links[0])
# class is  . id is #
# print(soup.select('.score'))


def create_custom_hn(links, votes):
    hn = []
    
    
    # loop thru the links get the text and append it to title
    for index, item in enumerate(links):
        title = links[index].getText()
        # get href or none
        href = links[index].get('href', None)
        
        import pdb 
        pdb.set_trace()
        hn.append(href)
    return hn 




print(create_custom_hn(links, votes))