import telebot, wikipedia, re
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('6117097971:AAEwrKYCtetbMkZnOCcC3h5EzKtLkfWBDkw')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(m.from_iser.id, "Привет! Я твой бот по Миру танков!", reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    
    if message.text == 'Поздороваться':
        markyp = types.ReplyKeyboardMarkup(resize_keyboard=True) # создание новых кнопок
        btn1 = types.KeyboardButton('Новости Мира танков!')
        btn2 = types.KeyboardButton('Статистика XVM')
        bth3 = types.KeyboardButton("Википедия")
        markyp.add(btn1, btn2, bth3)
        bot.send_message(message.from_user.id, 'Задайте интересующий вопрос', reply_markyp=markyp) #ответ бота

    elif message.text == 'Новости Мира танков!':
        bot.send_message(message.from_user.id, 'Новости' +'[ссылке](https://tanki.su/)', parse_mode='Markdown')

    elif message.text == 'Статистика XVM!':
        bot.send_message(message.from_user.id, 'Статистика' +'[ссылке](https://modxvm.com/ru/)', parse_mode='Markdown')
    
    elif message.text == 'Википедия':
        bot.send_message(message.chat.id, getwiki())
# Запускаем бота
bot.polling(none_stop=True, interval=0)

