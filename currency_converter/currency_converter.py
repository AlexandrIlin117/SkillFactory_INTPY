
import telebot
import my_token
import extensions


TOKEN = my_token.data_for_connect()
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_help(message, res=False):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}. Я помогаю в расчёте конвертации валют.\n"
                                      f"Сейчас я расскажу как мы это будем делать.\n"
                                      f"Всё просто:\n - дай мне команду '/values' и я выведу на экран "
                                      f"формат ввода валют для которых будем делать конвертацию;\n"
                                      f"- дай мне команду '/help' и я напомню что и как делать;\n"
                                      f"- дай мне команду '/start' и я снова поприветствую тебя :);"
                                      f"    \n"
                                      f"С командами разобрались теперь про формат ввода:\n"
                                      f"Введи через пробел валюту стоимость которой хочешь узнать,\n"
                                      f"затем ту валюту в какой хочешь узнать стоимость первой валюты,\n"
                                      f"ну и наконец для какого количества будем узнавать.\n"
                                      f"Получится вот так - 'EUR RUB 5'.\n"
                                      f"В случае ввода дробного числа используйте ТОЧКУ как разделитель!!!\n"
                                      f"Говоря вашим человеческим языком выясним - \n"
                                      f"'Сколько можно будет купить рублей за 5 евро?'\n"
                                      f"Я всё подсчитаю и дам ответ."
                                      f"Ну начали!!! Жду команд!!!")


@bot.message_handler(commands=['help'])
def handle_start_help(message, res=False):
    bot.send_message(message.chat.id, f"Формат ввода (вводить через пробел):\n"
                                      f"'EUR RUB 5'\n"
                                      f"что меняем например евро:     EUR \n"
                                      f"на что меняет например рубли: RUB \n"
                                      f"сколько евро меняем:          5\n"
                                      f"Я всё подсчтитаю и дам ответ.\n"
                                      f"В случае ввода дробного числа \n"
                                      f"используйте ТОЧКУ как разделитель!!!\n"
                                      f"Напоминаю команды:\n"
                                      f"'/values' - вывожу список валют;\n"
                                      f"'/start' - повтор приветствия;\n"
                                      f"'/help' - справка по работе с ботом;\n")


@bot.message_handler(commands=['values'])
def handle_start_help(message, res=False):
    bot.send_message(message.chat.id, f"Список волют доступных для конвертации:\n"
                                      f" {my_token.currency_display()}")


@bot.message_handler(content_types=['text'])
def handle_text_message(message: telebot.types.Message):
    try:
        if len(message.text) < 9:
            exp_arg = f"Нарушение формата ввода!\n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)

        base = message.text[:3]
        base = base.upper()
        if base not in my_token.currency_display():
            exp_arg = f"Код валюты КОТОРУЮ будем конвертировать не верен! \n" \
                      f"Используйте команду /values для поручения данных о правильном формате ввода буквенного кода валюты.\n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."

            raise extensions.APIException(exp_arg)
        if base in my_token.currency_display() and message.text[3] != " ":
            exp_arg = f"Нарушены правила ввода пропущен ПРОБЕЛ! \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)

        quote = message.text[4:7]
        quote = quote.upper()
        if quote not in my_token.currency_display():
            exp_arg = f"Код валюты В КОТОРУЮ будем конвертировать не верен! \n" \
                      f"Используйте команду /values для поручения данных о правильном формате ввода буквенного кода валюты.\n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)
        if quote in my_token.currency_display() and message.text[7] != " ":
            exp_arg = f"Нарушены правила ввода пропущен ПРОБЕЛ! \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)

        if base == quote:
            exp_arg = f"Конвертировать {base} в {quote} бессмысленно! \n" \
                      f"Но я оценил шутку! Потешаться на ботом, как это весело ... ХА ХА ХА ... Алиса!!! Мелафон!!! \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)

        amount = message.text[8:]
        if amount =='':
            exp_arg = f"Вы не указали какое КОЛИЧЕСТВО {base} будем конвертировать в {quote}!!! \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)

        for sym in amount:
            if sym.isdigit() is False and sym !=".":
                exp_arg = f"Недопустимый формат ввода количества валюты!!!\n" \
                          f"Количество валюты которую будем конвертировать нужно вводить используя цифры. \n" \
                          f"В случае ввода дробного числа используйте ТОЧКУ как разделитель!!! \n" \
                               f"Используйте команду /help для поручения информации о корректном формате ввода."
                raise extensions.APIException(exp_arg)
        separator_checking = 0
        for sym in amount:
            if sym == ".":
                separator_checking = separator_checking + 1
            if separator_checking > 1:
                exp_arg = f"Недопустимый формат ввода количества валюты!!!\n" \
                          f"Неправильное колличество РАЗДЕЛИТЕЛЕЙ!!! \n" \
                          f"В случае ввода дробного числа используйте ТОЧКУ как разделитель!!! \n" \
                          f"Используйте команду /help для поручения информации о корректном формате ввода."
                raise extensions.APIException(exp_arg)



        # if amount.isdigit() is False:
        #     exp_arg = f"Количество валюты которую будем конвертировать нужно указывать как ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ ЧИСЛО \n" \
        #               f"записаное ЦИФРАМИ без знака !!! \n" \
        #               f"Используйте команду /help для поручения информации о корректном формате ввода."
        #     raise extensions.APIException(exp_arg)


        if float(amount) <= 0:
            exp_arg = f"Значение количества конвертируемой валюты должно быть БОЛЬШЕ НУЛЯ !!! \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)
        if float(amount) >= 1e+168:
            exp_arg = f"Не думал что буду конвертировать такие огромные суммы для друга Била Гейтса !!! \n" \
                      f"К сожаление я могу поломаться если буду производить этот расчёт :( Введите число поменьше; \n" \
                      f"Используйте команду /help для поручения информации о корректном формате ввода."
            raise extensions.APIException(exp_arg)
        amount = float(amount)


    except extensions.APIException as e:
        bot.reply_to(message,f"Сбой!!! \n {e}")
    else:
        bot.reply_to(message, f"Сейчас порешаем, погоди ... \n"
                              f" {float(amount)} {base} это "
                              f"{extensions.SwitchWithApi.get_price(base, quote, float(amount))} "
                              f"{quote}")


bot.polling(none_stop=True)
