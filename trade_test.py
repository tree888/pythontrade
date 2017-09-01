import json
from zaifapi import *

#API設定
zaif_secret="your secret"
zaif_key="your key"

zaifP = zaifP = ZaifTradeApi(zaif_key, zaif_secret)

#トレード
status = zaifP.trade(currency_pair="btc_jpy", action="bid", price=530000, amount=0.001)
print(status)

