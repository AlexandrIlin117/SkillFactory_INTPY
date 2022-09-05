"""
extensions - Модуль содержит классы для организации запросов к API c котировками и отбработки исключений;
"""

import requests
import json

class SwitchWithApi:

    @staticmethod
    def get_price(base, quote, amount):
        response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        response = json.loads(response.text)
        result = response[quote] * amount
        return round(result, 2)


class APIException(Exception):
    """ This is my exception """










if __name__ == "__main__":
    print("Модуль запущен.")