class ProgramOptions:
    def __init__(self):
        self.program_choices = [
            "Программная инженерия",
            "Информационные системы и технологии (Технологии ИИ)",
            "Информационные системы и технологии (Программирование и системная интеграция IT-решений)",
            "Информатика и вычислительная техника"
        ]

    def display_program_options(self):
        print("\nДоступные направления:")
        for i, program in enumerate(self.program_choices, start=1):
            print(f"{i}. {program}")

    def get_program_choice(self):
        while True:
            choice = input("Введите номер направления: ")
            if choice.isdigit() and 1 <= int(choice) <= len(self.program_choices):
                return int(choice) - 1
            else:
                print("Некорректный выбор. Попробуйте ещё раз.")
