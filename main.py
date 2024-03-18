import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = "6914337127:AAEQT4sH761h62bBJCwySaBaoCtOl0h8Esw"
ACTIVE_USER = [1505278674, 7020358807]

bot = telebot.TeleBot(API_TOKEN)

rzd_info = '''[🚂] <b>Поезда РЖД</b>

1) <i>"Прибытие на вокзал"</i>
Приезжаем на вокзал, за <b>20-30 минут</b> до поезда.
Проходим "таможню". Сидим и ждем.

2) <i>"Объявление пути!"</i>
<b>Внимательно слушаем!</b> Так как говорят про <b>нумерацию вагонов!</b>
Рекомендую расположить паспорт в карман (в любое легкодоступное место).
Так как на морозе не всегда удобно доставать паспорт.

3) <i>"Идем на путь"</i>
<b>Если путь №1</b> - спускаемся
<b>Если путь №2-4</b> - идем по верхнему рукаву

4) <i>"Ищем вагон"</i>
<b>На местах проводников расположенны таблички с номером вагона</b>
p.s. Это слева вагона

5) <i>"Посадка в вагон"</i>
Говорить особо нечего, но всё же. Отдали паспорт проводнику, она всё проверила и отдала его обратно

6) <i>"Расположение в вагоне"</i>
<b>Документы не убираем!</b>
<b>Снизу под местом, есть место для вещей</b>
В следующем сообщении есть информация про твои места. 

7) <i>"Да сколько уже можно эти документы проверять!"</i>
После отправления, к нам должен подойти проводник, и снова проверить документы (такова инструкция)

8) <i>"Розетки"</i>
Розетки снизу под столом или на правой стене (на боковушке).

9) <i>"Можно и отдохнуть"</i>
<b>В принципе, всё.</b> Мы сели в поезд.

10) <i>"Рота подъем!"</i>
<b>За 30 минут до прибытия тебя разбудит проводник.</b> Так что можно поспать (правда без белья, ну и ладно)
Старайся заранее собрать вещи, ибо есть жесткая толкучка в самом вагоне при высадке.
За 7-8 минут до прибытия можно уже и надеть курточку :)'''

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button1 = telebot.types.KeyboardButton(text="Кнопка 1")
    # button2 = telebot.types.KeyboardButton(text="Кнопка 2")
    # button3 = telebot.types.KeyboardButton(text="Кнопка 3")
    keyboard.row("🚂 Поезд", "🏡 Общежитие")
    keyboard.row("🍽 Питание", "☺️ Мотивация")
    keyboard.row("👨‍💻 Работа")
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>Добро пожаловать в бота</b> 🤗\n\nДанному боту можешь написать только ты. \n<span class="tg-spoiler">Да-да, Эдя не может. В общем, это бот для тебя :)</span>\n\nЗдесь есть всякие <b>памятки и информация</b>.\nСнизу есть кнопочки, при помощи их ты можешь выбирать интересующие пункты.\n\np.s. Мотивация каждый день будет новая :D',
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@bot.message_handler(func=lambda message: True)
def main_block(message):
    if message.text == "🚂 Поезд": 
        bot.send_message(
            chat_id=message.chat.id,
            text=rzd_info,
            parse_mode="HTML"
        )
        bot.send_photo(
            chat_id=message.chat.id,
            parse_mode="HTML",
            photo="https://github.com/SergejWinston/Helper_bot/blob/main/16%20вагон.png?raw=true",
            caption='''<b>Отправление в НСК</b>
- Поезд <b>№116</b>
- Вагон <b>№16</b>
- Место <b>№35</b>
- Время отправления <b>04:56</b>
- Время прибытия <b>08:26</b>
- Время в пути <b>03:30</b>
- Паспорт РФ <b>5012 291727</b>
- <b>Без постельного белья</b>'''
        )
        
        bot.send_photo(
            chat_id=message.chat.id,
            parse_mode="HTML",
            photo="https://github.com/SergejWinston/Helper_bot/blob/main/10%20вагон.png?raw=true",
            caption='''<b>Отправление в БРБ</b>
- Поезд <b>№67</b>
- Вагон <b>№10</b>
- Место <b>№43</b>
- Время отправления <b>18:54</b>
- Время прибытия <b>22:55</b>
- Время в пути <b>04:01</b>
- Паспорт РФ <b>5012 291727</b>
- <b>Без постельного белья</b>'''
        )
    if message.text == "🏡 Общежитие": 
        print("home")
    if message.text == "🍽 Питание": 
        print("eat")
    if message.text == "☺️ Мотивация": 
        print("motivate")
    if message.text == "👨‍💻 Работа": 
        print("work")


bot.infinity_polling()