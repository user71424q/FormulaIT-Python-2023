class Device:
    """
    Базовый класс, представляющий устройство.
    Атрибуты:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
    Методы:
        __init__(self, brand: str, model: str): Инициализирует новое устройство.
        __str__(self): Возвращает строковое представление устройства.
        __repr__(self): Возвращает официальное строковое представление устройства.
        turn_on(self): Метод для включения устройства.
        support_contact_info(self): Метод для получения информации о службе поддержки.
    """
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        return f"Device(brand={self.brand!r}, model={self.model!r})"

    def turn_on(self) -> str:
        """
            Упрощенный метод включения устройства.
        """
        return "Устройство включено"

    def support_contact_info(self) -> str:
        """
            Возвращает контактную информацию службы поддержки для конкретного устройства.
        """
        ...


class Smartphone(Device):
    """
    Дочерний класс для смартфонов.
    Дополнительные атрибуты:
        _os (str): Операционная система смартфона, инкапсулированный атрибут.
    Методы:
        __init__(self, brand: str, model: str, os: str): Расширяет конструктор базового класса, делая операционную систему непубличной.
        os: Декоратор property для операционной системы, позволяющий читать значение.
        turn_on(self): Перегружает метод включения, добавляя специфичное для смартфонов поведение.
    """
    def __init__(self, brand: str, model: str, os: str) -> None:
        super().__init__(brand, model)
        self._os = os

    @property
    def os(self) -> str:
        """
        Геттер для операционной системы.
        Позволяет безопасно получить значение инкапсулированного атрибута _os.
        """
        return self._os

    def __str__(self) -> str:
        return f"{self.brand} {self.model} с ОС {self.os}"

    def __repr__(self) -> str:
        return f"Smartphone(brand={self.brand!r}, model={self.model!r}, os={self.os!r})"

    def turn_on(self) -> str:
        """
        Перегруженный метод включения устройства.
        Причина перегрузки: Добавление специфичного приветственного сообщения при включении смартфона.
        """
        return super().turn_on() + f". Загрузка {self.os}..."
