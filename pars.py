import requests
from bs4 import BeautifulSoup as bSoup
import telebot

API_KEY = '7270313248:AAGFRJugOdlp9cPr7FEkcgWhkN1w2GJcCh0'
URL = 'https://sfedu.ru/abitur/list/09.03.04_%D0%9A%D0%A2_%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F.%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%B8%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F_%D0%9E%D0%9E_%D0%93%D0%91'
URL2 = 'https://sfedu.ru/abitur/list/09.03.02_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B%20%D0%B8%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8.%20%D0%9F%D0%B5%D1%80%D1%81%D0%BF%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8_%D0%9E%D0%9E_%D0%93%D0%91'
def perser(url):
    r_get = requests.get(url)
    soup = bSoup(r_get.text, 'html.parser')
    table = soup.find_all('td')
    return [c.text for c in table]

list_applicants = perser(URL)

def place_on_the_list(list_applicants):
    daw = 1
    snils = input('введите снисл: ')
    for i in range(0, len(list_applicants)-1):
        if list_applicants[i] == snils:
            return list_applicants[i-1:i+17], daw
        elif list_applicants[i] == '✓':
            daw+=1

print(place_on_the_list(list_applicants))
bot = telebot.TeleBot(API_KEY)