import re

from src.job_processing import One_Vacancy


def chek_none(vacancy: dict, key: str, key2: str, meaning: str) -> str:
    if vacancy.get(key, {}) is not None:
        if vacancy.get(key).get(key2) is not None:
            return vacancy.get(key).get(key2)
        else:
            return meaning
    else:
        return meaning


def cast_to_object_list_new(json_list: list):
    """Перевод списка json в список объектов"""
    object_list = []
    for vacancy in json_list:
        object_list.append(
            One_Vacancy(
                vacancy["name"],
                chek_none(vacancy, "salary", "from", "0"),
                vacancy.get("alternate_url", "пусто"),
                chek_none(vacancy, "snippet", "requirement", "snippet"),
            )
        )
    return object_list


def cast_to_object_list(json_list: list):
    object_list = []
    for vacancy in json_list:
        object_list.append(
            One_Vacancy(
                vacancy["name"],
                str(vacancy["pay"]),
                vacancy.get("alternate_url", "пусто"),
                vacancy["snippet"],
            )
        )
    return object_list


def filtered_vacancies(filter_words: list, object_list: list) -> list:
    vacancy_filter = []
    for vacancy in object_list:
        for words in filter_words:
            print(vacancy.snippet)
            print(words)
            if re.search(words, vacancy.snippet) is not None:
                vacancy_filter.append(vacancy)
    return vacancy_filter


def get_top_vacancies(top_n: str, object_list):
    object_list = sorted(object_list, key=lambda x: x.pay, reverse=True)
    object_list = object_list[: int(top_n)]
    for vacancy in object_list:
        print(
            f"{vacancy.name} зарплата {vacancy.pay}, ссылка на вакансию {vacancy.url}, "
            f"краткое описание {vacancy.snippet}."
        )
