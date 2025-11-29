class Product:
    """Класс для описания продукта."""

    def __init__(self,name: str="Неизвестно",
                 code: str="Неизвестен",
                 quantity: int=0) -> None:
        """Инициализация/конструктор класса.

        Args:
            name: Наименование продукта.
            code: Шифр продукта.
            quantity: Количество продукта.
        """

        self.__name = name
        self.__code = code

        if quantity <= 0:
            while quantity <= 0:
                quantity = int(input('Пожалуйства введите количество продукта, большее 0: '))
                self.__quantity = quantity
        else:
            self.__quantity = quantity

    def get_name(self) -> str:
        """Геттер для наименования продукта.

        Returns:
            name: Наименование
        """

        return self.__name

    def get_code(self) -> str:
        """Геттер для шифра продукта.

        Returns:
            code: Шифр продукта.
        """

        return self.__code

    def get_quantity(self) -> int:
        """Геттер для количества продукта.

        Returns:
            quantity: Количество продукта.
        """

        return self.__quantity

    def set_name(self,name: str) -> None:
        """Сеттер для наименования продукта.

        Args:
            name: Наименование продукта.
        """

        self.__name = name

    def set_code(self,code: str) -> None:
        """Сеттер для шифра продукта.

        Args:
            code: Шифр продукта.
        """

        self.__code = code

    def set_quantity(self, quantity: int) -> None:
        """Сеттер для количества продукта.

        Args:
            quantity: Количество продукта.
        """

        while quantity <= 0:
            quantity = int(input('Пожалуйства введите количество продукта, большее 0: '))

        self.__quantity = quantity

    def display(self) -> None:
        """Вывод информации о продукте."""

        print(
            f'\nНаименование: {self.__name}\n'
            f'Шифр: {self.__code}\n'
            f'Количество: {self.__quantity}\n')

    def multiply_quantity(self,multiplier: int) -> None:
        """Функция, умножающее количество продукта на некоторый множитель, не равный нулю.

        Args:
            multiplier: Некоторый множитель, не равный нулю.
        """

        while multiplier <= 0:
            multiplier = int(input('Пожалуйста, введите множитель, больший 0 :'))

        self.__quantity *= multiplier

    def increase_quantity(self,amount: int) -> None:
        """Функция,увеличивающее количество продукта на некоторое число.

        Args:
            amount: Некоторое число.
        """

        self.__quantity += amount
