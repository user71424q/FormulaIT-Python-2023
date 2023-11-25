import doctest


class Book:
    def __init__(self, title: str, author: str, year_of_publication: int):
        """
        Инициализирует объект класса Book.

        :param title: Название книги, str.
        :param author: Автор книги, str.
        :param year_of_publication: Год издания, int.
        :raises TypeError: Если тип одного из параметров неверен.
        :raises ValueError: Если год издания отрицательный.

        Примеры:
        >>> book = Book("Война и Мир", "Лев Толстой", 1869)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Заголовок должен быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(year_of_publication, int) or year_of_publication < 0:
            raise ValueError("Год публикации должен быть неотрицательным целым числом")

        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication

    def get_info(self) -> str:
        """
        Возвращает информацию о книге в виде строки.

        :returns: Строка с информацией о книге, str.

        Примеры:
        >>> book = Book("Война и Мир", "Лев Толстой", 1869)  # инициализация экземпляра класса
        >>> book.get_info()
        """
        ...

    def update_year_of_publication(self, new_year: int) -> None:
        """
        Обновляет год издания книги.

        :param new_year: Новый год издания, int.
        :raises ValueError: Если новый год издания отрицательный.

        Примеры:
        >>> book = Book("Война и Мир", "Лев Толстой", 1869)  # инициализация экземпляра класса
        >>> book.update_year_of_publication(2023)
        """
        ...


class Smartphone:
    def __init__(self, model: str, operating_system: str, number: int):
        """
        Инициализирует объект класса Smartphone.

        :param model: Модель смартфона, str.
        :param operating_system: Операционная система смартфона, str.
        :param number: номер телефона, int.
        :raises TypeError: Если тип одного из параметров неверен.
        :raises ValueError: Если номер телефона отрицательный.

        Пример:
        >>> phone = Smartphone('Samsung s20', 'Android', 8805553535)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(operating_system, str):
            raise TypeError("Операционная система должна быть строкой")
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть целым неотрицательным числом")

        self.model = model
        self.operating_system = operating_system
        self.number = number

    def make_call(self, number: int) -> None:
        """
        Симулирует звонок на указанный номер.

        :param number: Номер телефона для звонка, int.
        :raises ValueError: Если номер телефона отрицательный.
        :returns: None.

        Пример:
        >>> phone = Smartphone('Samsung s20', 'Android', 8805553535)
        >>> phone.make_call(8980808080)
        """
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть целым неотрицательным числом")
        ...

    def install_app(self, app_name: str) -> None:
        """
        Симулирует установку приложения.

        :param app_name: Название приложения для установки, str.
        :returns: None.

        Пример:
        >>> phone = Smartphone('Samsung s20', 'Android', 8805553535)
        >>> phone.install_app("Google Chrome")
        """
        ...


class OnlineCourse:
    def __init__(self, title: str, instructor: str, duration: int):
        """
        Инициализирует объект класса OnlineCourse.

        :param title: Название курса, str.
        :param instructor: Имя преподавателя, str.
        :param duration: Длительность курса в часах, int.
        :raises TypeError: Если тип одного из параметров неверен.
        :raises ValueError: Если длительность курса отрицательная.

        Пример:
        >>> course = OnlineCourse("Python", "Иванов И.И.", 144)
        """
        if not isinstance(title, str):
            raise TypeError("Название курса должно быть строкой")
        if not isinstance(instructor, str):
            raise TypeError("Преподаватель должно быть строкой")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Длительность должна быть целым положительным числом")

        self.title = title
        self.instructor = instructor
        self.duration = duration

    def get_description(self) -> str:
        """
        Возвращает описание учебного курса.

        :returns: Описание курса, str.

        Пример:
        >>> course = OnlineCourse("Python", "Иванов И.И.", 144)
        >>> course.get_description()
        """
        ...

    def enroll_student(self, student_name: str) -> bool:
        """
        Добавляет студента на курс.

        :param student_name: Имя студента, str.
        :returns: Было ли добавление успешным, bool.

        Пример:
        >>> course = OnlineCourse("Python", "Иванов И.И.", 144)
        >>> course.enroll_student("Петров П.П.")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
