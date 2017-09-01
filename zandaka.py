import json
from zaifapi import *

zaif_secret="your secret"
zaif_key="your key"

zaif = ZaifPublicApi()
zaifP = ZaifTradeApi(zaif_key, zaif_secret)

ZaifFunds=zaifP.get_info()
ZaifJPY=ZaifFunds['funds']['jpy']
ZaifBTC=ZaifFunds['funds']['btc']

print("JPY:",ZaifJPY,"BTC:",ZaifBTC)
