from pymarketcap import Pymarketcap
coinmarketcap = Pymarketcap()
XEM = coinmarketcap.markets('XEM')

for i in range(len(XEM)):

    if 'ETH' in XEM[i]['pair']:
        print(XEM[i])