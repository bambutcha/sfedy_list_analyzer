from program_options import ProgramOptions
from menu import MainMenu
from data_manager import DataManager

class UniversityApplicationSystem:
    def __init__(self):
        self.program_options = ProgramOptions()
        self.main_menu = MainMenu()
        self.data_manager = DataManager()

    def run(self):
        student_snils = input("Введите СНИЛС студента: ")
        self.program_options.display_program_options()
        program_choice = self.program_options.get_program_choice()
        self.main_menu.display_menu()
        menu_choice = self.main_menu.get_menu_choice()
        student_data = self.data_manager.get_student_data(program_choice, student_snils)
        if student_data is None:
            return "СНИЛС введен неверно. Пожалуйста, попробуйте еще раз."
        else:
            message = self.data_manager.format_student_data(student_data)
            return message
