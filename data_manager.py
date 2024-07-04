import requests
from bs4 import BeautifulSoup as bSoup

class DataManager:
    def __init__(self):
        self.program_urls = [
            "https://sfedu.ru/abitur/list/09.03.04_%D0%9A%D0%A2_%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F.%20%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B%20%D0%B8%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%20%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F_%D0%9E%D0%9E_%D0%93%D0%91",
            "https://sfedu.ru/abitur/list/09.03.01_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B0_%D0%9E%D0%9E_%D0%93%D0%91",
            "https://sfedu.ru/abitur/list/09.03.01_%D0%9A%D0%A2_%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0.%20%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82%D0%B0_%D0%9E%D0%9E_%D0%93%D0%91"
        ]

    def get_student_data(self, program_index: int, student_snils: str) -> list:
        response = requests.get(self.program_urls[program_index])
        soup = bSoup(response.text, 'html.parser')
        table_cells = soup.find_all('td')
        table_data = [cell.text for cell in table_cells]
        application_count = 0
        for i in range(0, len(table_data)-1):
            if table_data[i] == student_snils:
                student_data = table_data[i-1:i+17]
                student_data.append(application_count)
                return student_data
            elif table_data[i] == '✓':
                application_count += 1
        return None

    def format_student_data(self, student_data: list) -> str:
        highest_priority = student_data[17] if student_data[17] else '🚫'
        return f"Ваше место: {student_data[0]}. СНИЛС: {student_data[1]}. Приоритет специальности: {student_data[2]}. Сумма баллов: {student_data[7]}. Все направления: {student_data[15]}. Высший приоритет: {highest_priority}. Ваше место по приоритету: {student_data[18]}."
