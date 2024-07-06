import requests
from bs4 import BeautifulSoup as bSoup
import telebot
from telebot import types

API_KEY = '###'
URL = [
            "https://sfedu.ru/abitur/list/09.03.04_%D0%9A%D0%A2_%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F.%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%B8%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F_%D0%9E%D0%9E_%D0%93%D0%91",
            "https://sfedu.ru/abitur/list/09.03.01_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B0_%D0%9E%D0%9E_%D0%93%D0%91",
            "https://sfedu.ru/abitur/list/09.03.01_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%98%D0%A2-%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B9_%D0%9E%D0%9E_%D0%93%D0%91",
            "https://sfedu.ru/abitur/list/09.03.02_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B%20%D0%B8%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8.%20%D0%9F%D0%B5%D1%80%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8_%D0%9E%D0%9E_%D0%93%D0%91"
        ]

snils = ''

def parse_url(url):
    r_get = requests.get(url)
    soup = bSoup(r_get.text, 'html.parser')
    table = soup.find_all('td')
    return [c.text for c in table]

def find_place_in_list(snils, parsed_site):
    daw = 1
    for i in range(0, len(parsed_site) - 1):
        if parsed_site[i] == snils:
            return parsed_site[i - 1:i + 17], daw
        elif parsed_site[i] == '✓':
            daw += 1
    return None, daw

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
    
def ask_for_snils(message):
    bot.send_message(message.chat.id, "Приветствую! Я бот, который поможет тебе отслеживать свою позицию в конкурсных списках на поступление в ВУЗ.\n\nДля начала, пожалуйста, введи свой СНИЛС(111-222-333 44): ")
    bot.register_next_step_handler(message, ask_for_direction_number)

def ask_for_direction_number(message):
    global snils
    snils = message.text
    if len(snils) != 14:
        bot.send_message(message.chat.id, 'Пожалуйста, введите СНИЛС по образцу!')
        bot.register_next_step_handler(message,ask_for_direction_number)
        return
    else:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Программная инженерия', callback_data='0')
        btn2 = types.InlineKeyboardButton('Информатика и вычислительная техника (Технологии ИИ)', callback_data='1')
        btn3 = types.InlineKeyboardButton('Информатика и вычислительная техника (Программирование и системная интеграция IT-решений)', callback_data='2')
        btn4 = types.InlineKeyboardButton('Информационные системы и технологии', callback_data='3')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Введите номер направления!\nДоступные направления:',reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def process_snils(call):
    direction_number = call.data
    list_applicants = parse_url(URL[int(direction_number)])
    parsed_site_slice, daw_value = find_place_in_list(snils, list_applicants)
    
    if parsed_site_slice is not None:
        highest_priority = parsed_site_slice[17] if parsed_site_slice[17] else '🚫'
        combined_text = f"Ваше место: {parsed_site_slice[0]}. СНИЛС: {parsed_site_slice[1]}. Приоритет специальности: {parsed_site_slice[2]}. Сумма баллов: {parsed_site_slice[7]}. Все направления: {parsed_site_slice[15]}. Высший приоритет: {highest_priority}. Ваше место по приоритету: {daw_value}."
        bot.send_message(call.message.chat.id, combined_text)
        bot.register_next_step_handler(call.message, ask_for_direction_number)
    else:
        bot.send_message(call.message.chat.id, "СНИЛС не найден в списке.")

bot.polling()