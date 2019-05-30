from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN = 'pk_87301e7c4b334621abd8a06136d1178e'

aapl = Stock('AAPL', token=TOKEN)
fb = Stock('FB', token=TOKEN)

data = aapl.get_quote()
# print(data)
pp.pprint(data)

print(data['companyName'], data['latestPrice'])


