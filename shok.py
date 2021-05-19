from telebot import types
import time
import telebot
bot = telebot.TeleBot("1676185607:AAFNC5_95z2L9ZcQCq0lZGOz0gX8iZBdn1U")

def glm():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('🏠 Локации 🏠', callback_data='loc'),
            types.InlineKeyboardButton('📦 Покупки 📦', callback_data='poc'))
    key.row(types.InlineKeyboardButton('💬Связь с администрацией💬', callback_data='svya'))
    key.row(types.InlineKeyboardButton('Оператор️', callback_data='oper'))
    key.row(types.InlineKeyboardButton('Работа в магазине️', callback_data='rab'))
    return key

def nazad ():
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton('↩ Назад', callback_data='glm'))
    return key

def loci():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Минусинск', callback_data='minus'))
    key.row(types.InlineKeyboardButton('Абакан', callback_data='abak'))
    key.row(types.InlineKeyboardButton('↩ Назад', callback_data='glm'))
    return key

def tov():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Тв 1г JVH2,2 - 1300 RUB ', callback_data='opl1'))
    key.row(types.InlineKeyboardButton('Тв 3г JVH2,2 - 2300 RUB ', callback_data='opl2'))
    key.row(types.InlineKeyboardButton('↩ Назад', callback_data='glm'))
    return key

def tov2():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Тв 5г JVH2,2 - 3500 RUB ', callback_data='opl3'))
    key.row(types.InlineKeyboardButton('↩ Назад', callback_data='glm'))
    return key

def btc ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse01'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key

def btc1 ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse1'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse11'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key

def btc2 ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse2'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse22'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key

def btc3 ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse3'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse33'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key
def btc11 ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse1'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse11'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key
def btc22 ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse1'))
    key.row(types.InlineKeyboardButton('Оплата Qiwi', callback_data='vse11'))
    key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
    return key

# def btc2 ():
#     key = types.InlineKeyboardMarkup()
#     key.row(types.InlineKeyboardButton('Оплата BTC', callback_data='vse2'))
#     key.row(types.InlineKeyboardButton(' ↩Назад', callback_data='glm'))
#     return key

def check ():
    key = types.InlineKeyboardMarkup()
    key.row(types.InlineKeyboardButton('Проверить оплату', callback_data='check'))
    key.row(types.InlineKeyboardButton('↩ Назад', callback_data='glm'))
    return key


@bot.message_handler(commands=["start"])
def inline(message):
	bot.send_message(message.chat.id, "Добро пожаловать в наш магазин",
	 reply_markup=glm())

x='@Mc_ShockADM'

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    global x
    if c.data=='otk':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Очень долго я и мой подельник искали способ монетизировать кредитные карты, которые он покупал в даркнете у людей с форумов. Мы пробовали покупать товары, но счета сразу же замораживались. Пытались работать с людьми знающими, но натыкались только на развод. "
            "\nСпустя несколько месяцев раздумий, проб и ошибок у меня все-таки получилось найти способ вытащить деньги с карт американцев полностью анонимно — решением оказались ваучеры киви, которые ты активируешь, и на кошелек поступает сумма равная сумме ваучера."
			"\nВывести эти деньги все и сразу у нас не получается, банк начинает звонить и задавать вопросы по типу 'откуда у вас 80 тысяч на карте с разных счетов? У вас есть незарегестрированный в налоговой бизнес?'. Пообщавшись с моим коллегой мы решили, что лучшим решением будет продавать эти кошельки другим людям, чтобы раскидать эти деньги по разным точкам России и СНГ более равномерно, а также обойти вопросы банка. "
			"\nЯ создал этого бота с автоматизированной выдачей кошельков из базы данных, которую заполняет мой коллега. Надеюсь, что в этих словах вы найдете ответ на постоянные вопросы 'Как можно продавать деньги за деньги?',  'А что же вы сами тогда не выводите?' и т.п."
			"\n======================================"
			"\nПринцип работы моего бота таков. После выбора кошелька и его оплаты, вы вписываете номер счета с которого оплачивали, бот сверяет, и если всё верно, то выдает вам номер киви кошелька и пароль. Как только вы вводите данные для входа в кошелек в приложение, и оно запрашивает смс-код, бот тут же высылает вам проверочный код(все кошельки привязаны на виртуальные номера, арендованные на месяц, доступ к которым есть у бота). Как только вы вошли в кошелек и проверили баланс, можете выходить и заходить снова, бот будет выдавать коды в течение месяца с добавления кошелька(следите за обновлениями в группе с отзывами). Для того чтобы вывести деньги вам также потребуется код, который вам выдаст наш бот. ВНИМАНИЕ! ЗАПОМНИТЕ! СМС ПОДТВЕРЖДЕНИЯ НА КИВИ КОШЕЛЬКАХ НЕ ОТКЛЮЧАЮТСЯ!!! Те, кто вам такое говорит, промышляют обманом."
			"\n======================================"
			"\nТеперь ответы на частозадаваемые вопросы:"
			"\n- Деньги можно вывести куда угодно, будь то карта/ваш киви кошелек/любой другой электронный кошелек, также можно оплатить какой-либо товар из интернета;"
			"\n- Больше одного кошелька в день бот вам не выдаст, это сделано для нашей и вашей безопасности, поэтому если вы попытаетесь купить второй кошелек, то бот просто оформит возврат средств на ваш счет;"
			"\n- Такой отмыв денег не нарушает ни одного закона Российской Федерации и близ расположенных стран, т.к. по сути все что мы делаем это выкачиваем деньги из гос. бюджета Америки в Россию. Владельцы карт всегда получают возврат средств по страховке в размере 90%, потому мы крадем у их страховой, а не у них. Иными словами, нет ни малейшего повода для волнения, спим спокойно :)"
			"\n======================================"
			"\nТелеграм канал со всей информацией по поводу бота teleg.run/joinchat/AAAAAEajQiSplkpZm855cA"
			"\nСвязь со мной @voprosisuda"
			"\nПосле покупки кошелька вы можете написать отзыв мне в личку и получить скидку до 40% на следующий кошелек!",
            parse_mode="markdown",
            reply_markup=nazad ())
    elif c.data=='glm':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Добро пожаловать в наш магазин",
            parse_mode="markdown",
            reply_markup=glm ())
    elif c.data=='loc':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Выберите город:",
            parse_mode="markdown",
            reply_markup=loci ())
    elif c.data=='poc':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="У вас пока не было покупок.",
            parse_mode="markdown",
            reply_markup=nazad ())
    elif c.data == 'svya':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text=f'По всем вопросам обращаться @Mc\_Shock\_ADM ',
            parse_mode="markdown",
            reply_markup=nazad())
    elif c.data == 'oper':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Оператор магазина @Mc\_Shock\_TB  ",
            parse_mode="markdown",
            reply_markup=nazad())
    elif c.data == 'rab':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="По поводу работы писать @Mc\_Shock\_ADM ",
            parse_mode="markdown",
            reply_markup=nazad())
    elif c.data == 'minus':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Выберите товар:",
            parse_mode="markdown",
            reply_markup=tov())
        x="2 520 ₽"
    elif c.data == 'abak':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Выберите товар:",
            parse_mode="markdown",
            reply_markup=tov2())
    elif c.data=='kosh5':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="К оплате 7 560 ₽ \n➖➖➖➖➖➖➖➖➖➖\n Выберите способо оплаты (Способы оплаты в будущем будут пополняться):",
            parse_mode="markdown",
            reply_markup=qiwi ())
        x="7 560 ₽"
    elif c.data=='opl':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите способ оплаты:',
            parse_mode="markdown",
            reply_markup=btc ())
    elif c.data=='opl1':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите способ оплаты:',
            parse_mode="markdown",
            reply_markup=btc1 ())
    elif c.data=='opl2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите способ оплаты:',
            parse_mode="markdown",
            reply_markup=btc2 ())
    elif c.data == 'opl3':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите способ оплаты:',
            parse_mode="markdown",
            reply_markup=btc3())
    elif c.data == 'opl2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите способ оплаты:',
            parse_mode="markdown",
            reply_markup=btc2())
    elif c.data=='vse':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1213\n\nВы приобретаете:\n 📦 Тв (new) ОПТ ОТ 20гр\n\nЛокация:\n🌇 Минусинск\n\nДля покупки, переведите на blockchain кошелек:\n1JUQDrrH8JGPGJGFioTx2BMv1S5Y3JeWrN\nсумму:\n0,001601 BTC,\n❗️ Оплату производить точной суммой BTC и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 0,001601 BTC на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse1':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1254\n\nВы приобретаете:\n 📦 Тв 1г JVH2,2\n\nЛокация:\n🌇 Минусинск\n\nДля покупки, переведите на blockchain кошелек:\n1JUQDrrH8JGPGJGFioTx2BMv1S5Y3JeWrN1\nсумму:\n0.000385 BTC,\n❗️ Оплату производить точной суммой BTC и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 0.000385 BTC на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse2':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1212\n\nВы приобретаете:\n 📦 Тв 3г JVH2,2\n\nЛокация:\n🌇 Минусинск\n\nДля покупки, переведите на blockchain кошелек:\n1JUQDrrH8JGPGJGFioTx2BMv1S5Y3JeWrN\nсумму:\n0.000681 BTC,\n❗️ Оплату производить точной суммой BTC и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 0.000681 BTC на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse3':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1211\n\nВы приобретаете:\n 📦 Тв 5г JVH2,2\n\nЛокация:\n🌇 Абакан\n\nДля покупки, переведите на blockchain кошелек:\n1JUQDrrH8JGPGJGFioTx2BMv1S5Y3JeWrN\nсумму:\n0.001036 BTC,\n❗️ Оплату производить точной суммой BTC и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 0.001036 BTC на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse11':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1215\n\nВы приобретаете:\n 📦 Тв 1г JVH2,2\n\nЛокация:\n🌇 Минусинск\n\nДля покупки, переведите на Qiwi кошелек:\n+79515586641\nсумму:\n1300 RUB,\n❗️ Оплату производить точной суммой RUB и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 1300 RUB на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse22':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1225\n\nВы приобретаете:\n 📦 Тв 3г JVH2,2\n\nЛокация:\n🌇 Минусинск\n\nДля покупки, переведите на Qiwi кошелек:\n+79515586641\nсумму:\n2300 RUB,\n❗️ Оплату производить точной суммой RUB и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 2300 RUB на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='vse33':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="🛄 Заказ #1229\n\nВы приобретаете:\n 📦 Тв 5г JVH2,2\n\nЛокация:\n🌇 Абакан\n\nДля покупки, переведите на Qiwi кошелек:\n+79515586641\nсумму:\n3500 RUB,\n❗️ Оплату производить точной суммой RUB и одним платежом, иначе платеж не будет учтен. Для вас был зарезервирован товар на 30 минут. В течении 30 минут переведите 3500 RUB на счет.",
            parse_mode="markdown",
            reply_markup=check ())
    elif c.data=='check':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Проводится проверка платежа, примерное время ожидания 1-5мин",
            parse_mode="markdown")
        time.sleep(90)
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Платеж не был найден, повторите проверку позже",
            parse_mode="markdown",
            reply_markup=check())
    



if __name__ == "__main__":
    bot.polling(none_stop=True)
