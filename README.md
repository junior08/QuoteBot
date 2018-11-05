# QuoteBot
A slack- bot which automates the process of wishing people and can be configured to send quotes along with that- at a user scheduled time.

This bot uses a given channel on Slack, on this  channel, it sends automated Quotes or wishes depending on the needs of the user.

The quotes are scraped from a website using BeautifulSoup and saved in the form of a list/array.
When called, QuoteBot picks up a random quote fromt this collection and sends it to the desired channel.
However, it can also be configured to wish at a particular time every day, hence removing the need for monotonous wishing.

![](https://github.com/junior08/QuoteBot/blob/master/bot.PNG)
