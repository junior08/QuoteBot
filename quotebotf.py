import lxml
import schedule
import time
from slackclient import SlackClient
import random
import bs4 as bs
import urllib.request#Importing all the necessary libraries

qt = []
sauce = urllib.request.urlopen('http://wisdomquotes.com/love-quotes/').read()#Seding a request to the website where we scrape the quotes from
soup = bs.BeautifulSoup(sauce, 'lxml')#Converting it to a soup object

for quote in soup.find_all('blockquote'):# Getting all the quotes and appending them to a list
    qt.append(quote.text.split('.')[0] + '.')



def slack_quote():
    quote_new = random.choice(qt)#Randomly picking up a quote
    
    token = 'your token here'#Your slack legacy token here
    sc = SlackClient(token)
    
    history = sc.api_call('channels.history', channel = 'the channel-code')# Getting the history of a particular channel, replace with your channel code

    command = history['messages'][0]['text']

    if 'quotebot' in command:#Checking if the bot was called

        sc.api_call('chat.postMessage', channel = '#general', text = quote_new, username='Quotebot', icon_emoji = ':robot_face:')#Posting a quote
        return 1
    return 0


schedule.every(2).seconds.do(slack_quote)#The bot checks every 2 seconds if it was called
while True:
    schedule.run_pending()
    time.sleep(1)

 


