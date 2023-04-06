from CryptoPrice import get_default_retriever
from datetime import datetime

retriever = get_default_retriever()


def ETHUSDT():
    """
    :return: Возвращает текущую цену Эфира в USDT указанная в Binance
    """
    timestamp = int(datetime.now().timestamp())
    return retriever.get_closest_price('ETH', 'USDT', timestamp).value


def BTCUSDT():
    """
    :return: Возвращает текущую цену Биткоина в USDT указанная в Binance
    """
    timestamp = int(datetime.now().timestamp())
    return retriever.get_closest_price('BTC', 'USDT', timestamp).value
