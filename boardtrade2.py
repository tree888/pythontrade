import time
from zaifapi import *

zaif_secret="your secret"
zaif_key="your key"

zaif = ZaifPublicApi()
zaifP = ZaifTradeApi(zaif_key, zaif_secret)


#トレードしたい通貨
pair = "btc_jpy"


while True:
    #板情報の取得
    zaif_board_data = zaif.depth(pair)
    ask_price = zaif_board_data['asks'][0][0]
    ask_amount = zaif_board_data['asks'][0][1]
    bid_price = zaif_board_data['bids'][0][0]
    bid_amount = zaif_board_data['bids'][0][1]

    print("AskPrice:",ask_price,"BidPrice:",bid_price)

    #トレード
    if (ask_price < 430000 ):
        status = zaifP.trade(currency_pair=pair, action="bid", price=int(ask_price), amount=0.001)
        #売り注文 status = zaifP.trade(currency_pair=pair, action="ask", price=int(bid_price), amount=0.001)
        print(status)


    #インターバル
    time.sleep(60)