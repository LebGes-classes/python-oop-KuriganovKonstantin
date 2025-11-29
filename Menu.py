from Product import (
    Product,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def print_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\nВыбор действий:\n'
            '1.Получить информацию о наименовании продукта.\n'
            '2.Получить информацию о шифре продукта.\n'
            '3.Получить информацию о количестве продукта.\n'
            '4.Изменить наименование продукта.\n'
            '5.Изменить шифр продукта.\n'
            '6.Изменить количество продукта.\n'
            '7.Просмотр информации о продукте.\n'
            '8.Умножить количество на число.\n'
            '9.Добавить к количество число.\n'
            '10.Завершить программу\n'
        )

    def main_menu(self,choice: int ,
                  product: Product) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: Выбор, введённый пользователем.

        Returns:
            the_end_of_the_program: Конец ли программы.
        """

        the_end_of_the_program = False


        match choice:
            case 1:
                print(f"Наименование продукта: {product.get_name()}")
            case 2:
                print(f"Шифр продукта: {product.get_code()}")
            case 3:
                print(f"Количество продукта: {product.get_quantity()}")
            case 4:
                new_name = input('Введите новое имя: ')

                product.set_name(new_name)
            case 5:
                new_code = input('Введите новый шифр: ')

                product.set_code(new_code)
            case 6:
                new_quantity = int(input('Введите новое количество: '))

                product.set_quantity(new_quantity)
            case 7:
                product.display()
            case 8:
                multiplier = int(input('Введите множитель: '))

                product.multiply_quantity(multiplier)
            case 9:
                amount = int(input('Введите слагаемое: '))

                product.increase_quantity(amount)
            case 10:
                the_end_of_the_program = True
            case _:
                print('Ошибка. Нет такого выбора.')

        return the_end_of_the_program
