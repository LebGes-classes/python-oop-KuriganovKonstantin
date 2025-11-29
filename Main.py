from Product import (
    Product,
)
from Menu import (
    Menu,
)

class Main:
    """Класс для демонстрации работы классов меню и продукта."""

    menu = Menu()
    product_1 = Product()
    product_2 = Product('Milk', '0429435', 3124)


    def run(self) -> None:
        """Метод запуска работы."""

        the_end_of_the_program = False

        while not the_end_of_the_program:
            self.menu.print_menu()

            choice = int(input('Введите выбор: '))
            choice_product = int(input('Введите порядковый номер продукта: '))

            product = self.product_1 if choice_product == 1 else self.product_2

            the_end_of_the_program = self.menu.main_menu(choice,product)

            useless_input = input('Нажмите любую клавишу, чтобы продолжить.')


Main().run()
