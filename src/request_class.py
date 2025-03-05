from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Абстрактный класс для API"""

    __url: str
    __headers: dict
    __params: dict
    vacancies: list

    @abstractmethod
    def _load_vacancies(self, *args):
        pass

    @abstractmethod
    def get_vacancies(self, *args) -> list:
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def _load_vacancies(self, keyword):
        """Подгрузка вакансий"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    def get_vacancies(self, keyword) -> list:
        """Выдача вакансий"""
        self._load_vacancies(keyword)
        return self.__vacancies
