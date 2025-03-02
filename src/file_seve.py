import json
from abc import ABC, abstractmethod


class Abstract_Json(ABC):
    """Абстрактный класс для json файла"""

    __filename: str

    @abstractmethod
    def json_give(self):
        pass

    @abstractmethod
    def json_save(self, *args):
        pass

    @abstractmethod
    def json_delite(self, *args):
        pass


class Json(Abstract_Json):
    """Класс для json файла"""

    def __init__(self, keyword):
        self.__filename = f"{keyword.title()}.json"
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump([], file)

    def json_give(self):
        with open(self.__filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def json_save(self, list_object):
        """Записывает информацию в файл с фильтром на дубликаты"""
        old_vacancies = self.json_give()
        new_list = []
        if old_vacancies == []:
            for vacancy_new in list_object:
                new_list.extend(vacancy_new.vacancy_dict)
            old_vacancies.extend(new_list)
        else:
            for vacancy in old_vacancies:
                for index, new_vacancy in enumerate(list_object):
                    if vacancy.get("name", "pass") == new_vacancy.name:
                        list_object.pop(index)
            for vacancy_new in list_object:
                old_vacancies.extend(vacancy_new.vacancy_dict)

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file, indent=4, ensure_ascii=False)

    def json_delite(self, vacansy_name: str):
        old_vacancies = self.json_give()
        for index, vacancy in enumerate(old_vacancies):
            if vacancy.get("name", "pass") == vacansy_name:
                old_vacancies.pop(index)
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(old_vacancies, file, indent=4, ensure_ascii=False)
