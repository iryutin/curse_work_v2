class One_Vacancy:
    """Класс с вакансиями"""

    __slots__ = ("name", "pay", "url", "snippet")
    pay: str
    name: str
    url: str
    snippet: str

    def __init__(self, name, pay, url, snippet):
        self.pay = pay
        self.name = name
        self.url = url
        self.snippet = snippet

    def __call__(self, other):
        """Сравнение зп"""
        if type(self) is type(other):
            if self.pay > other.pay:
                print(f"Вакансия {self.name} более оплачиваемая")
            elif self.pay < other.pay:
                print(f"Вакансия {other.name} более оплачиваемая")
            else:
                print("Зарплата равна")
        else:
            raise TypeError

    @property
    def vacancy_dict(self):
        """Конвертация в словарь"""
        new = [
            {
                "name": self.name,
                "pay": self.pay,
                "url": self.url,
                "snippet": self.snippet,
            }
        ]
        return new
