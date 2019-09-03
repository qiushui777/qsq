import logging

def signal_day_back_test(account=None ,buysignal=None, sellsignal=None):
    """
    择时策略日线回测
    param: account 帐户
    param: buysignal 购买信号，用户自己实现
    param: sellsignal 卖出信号，用户自己实现
    """
    logging.info("start back test...")
    df = buysignal.crypto.crypto_df
    for date_index in df.index:
        date_str = str(date_index.date())

        # 判断买点
        # TODO: signal返回购买费用/比例 
        buy_result = buysignal.produce_signal(date_index)
        if buy_result['mode'] == 1 and account.trade == True and account.balance > 1000:
            buy_price = df.loc[date_index]['close']
            buy_amount = int((account.balance*buy_result['percent'])/(buy_price*(1+account.commission)))
            account.Order(date=date_str,time='19:00',mode=1,symbol=buy_result['symbol'],amount=buy_amount,
                        price=buy_price)
            logging.info(date_str + " buy " + buy_result['symbol'] + ' ' + str(buy_amount))
            logging.info("The balance is " + str(account.balance))

        # 判断卖点
        sell_result = sellsignal.produce_signal(date_index)
        if sell_result['mode'] == 2 and account.symbol_amount(sell_result['symbol']) > 0:
            sell_price = df.loc[date_index]['close']
            sell_amount = account.symbol_amount(sell_result['symbol'])*sell_result['percent']
            account.Order(date=date_str,time='19:00',mode=2,symbol=sell_result['symbol'],amount=sell_amount,
                        price=sell_price)
            logging.info(date_str + " sell " + sell_result['symbol'] + ' ' + str(sell_amount))
            logging.info("The balance is " + str(account.balance))

        # 判断是否止损
        close_price = df.loc[date_index]['close']
        if account.symbol_amount(sell_result['symbol']) > 0 and close_price < account.stop_loss_price[sell_result['symbol']]:
            sell_amount = account.symbol_amount(sell_result['symbol'])
            account.Order(date=date_str,time='19:00',mode=2,symbol=sell_result['symbol'],amount=sell_amount,
                        price=close_price)
            account.stop_loss_num += 1
            logging.info(date_str + " stop loss " + sell_result['symbol'] + ' ' + str(sell_amount))
            logging.info("The balance is " + str(account.balance))