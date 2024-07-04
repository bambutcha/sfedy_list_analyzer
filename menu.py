class MainMenu:
    def display_menu(self):
        print("\nМеню:")
        print("1. Посмотреть себя в списке")
        print("2. Узнать общее количество подавших заявления")

    def get_menu_choice(self):
        while True:
            choice = input("\nВведите номер пункта меню: ")
            if choice == "1":
                return 1
            elif choice == "2":
                return 2
            else:
                print("Некорректный выбор. Попробуйте еще раз.")