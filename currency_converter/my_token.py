"""
my_token - Модуль содержит строку для доступа к HTTP API моего бота;
         - Так же модуль содержит функцию возвращающую строку с валютами доступными для конвертации;
"""

def data_for_connect():
    bot_token = "--- На этом месте мог бы быть ваш ТОКЕН ---"
    return bot_token

def currency_display():
    curr_dict_str = []
    currency_dictionary = {'USD': 'Доллар США',
                           'EUR': 'Евро',
                           'GBP': 'Фунт стерлингов',
                           'CNY': 'Китайский юань',
                           'TRY': 'Турецкая лира',
                           'RUB': 'Российский рубль',
                           'JPY': 'Японская Иена',
                           'AED': 'ОАЭ дихрам',
                           'THB': 'Тайландский бат',
                           'INR': 'Индийская рупия', }
    for key, value in currency_dictionary.items():
        curr_dict_str.append(f"{key} : {value}")
    curr_dict_str = "\n".join(curr_dict_str)
    return curr_dict_str


if __name__ == "__main__":
    print("Модуль запущен.")