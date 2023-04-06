from crypto_api import ETHUSDT, BTCUSDT, datetime
from time import sleep


class EthTracker:
    def __init__(self):
        self.eth_price = ETHUSDT()  # Текущая цена эфира в USDT
        self.btc_price = BTCUSDT()  # Текущая цена биткоина в USDT
        self.last_check_time = datetime.now()  # Последний раз когда проверялась собственная цена Эфира
        self.eth_change_USDT = 0  # Собственное изменение цены Эфира за последний интервал
        self.threshold_for_check = 1  # %  # Величина изменения собственного движения Эфира, чтобы вывести значение
        self.interval_time = 60*60  # Время в секундах через которое нужно проверять собственную цену Эфира

    def track(self):
        while True:
            self.last_check_time = datetime.now()
            print(f"\nВремя проверки: {self.last_check_time}")
            print(f"Текущая цена за Эфир: {self.eth_price}$")
            print(f"Текущая цена за Биткоин: {self.btc_price}$")

            eth_change = self.eth_own_change()

            if abs(eth_change) > self.threshold_for_check:
                print(f"Собственное изменение цены Эфира: {round(eth_change*100, 2)}%")
                print(f"Собственное изменение цены Эфира в долларах: {self.eth_change_USDT}$")
            else:
                print(f"Собственное изменение Эфира за последний раз не больше {self.threshold_for_check}%.")
            print(f"Следующая проверка через {self.interval_time/60} минут.")
            sleep(self.interval_time)

    def eth_own_change(self):
        """
        Возвращает собственное процентное изменение цены ETHUSDT
        """
        current_eth_price, current_btc_price = ETHUSDT(), BTCUSDT()

        eth_change = self.calc_percent_change(self.eth_price, current_eth_price)
        btc_change = self.calc_percent_change(self.btc_price, current_btc_price)

        self.eth_change_USDT = current_eth_price - self.eth_price
        self.eth_price, self.btc_price = current_eth_price, current_btc_price

        return eth_change - btc_change

    @staticmethod
    def calc_percent_change(previous_price, current_price):
        """
        :param previous_price: Прошлая цена валюты
        :param current_price: Настоящая цена валюты
        :return: Возвращает процентное изменение цены валюты
        """
        return (current_price - previous_price) / previous_price


if __name__ == "__main__":
    tracker = EthTracker()
    tracker.track()
