from src.file_seve import Json
from src.request_class import HeadHunterAPI
from src.support_function import (
    cast_to_object_list,
    cast_to_object_list_new,
    filtered_vacancies,
    get_top_vacancies,
)


def user():
    hh_api = HeadHunterAPI()

    keyword = input("Введите поисковый запрос: ")
    json_file = Json("vacancies")

    json_file.json_save(cast_to_object_list_new(hh_api.get_vacancies(keyword)))

    list_object = cast_to_object_list(json_file.json_give())

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    list_object_filter = filtered_vacancies(filter_words, list_object)

    top_n = input("Введите количество вакансий для вывода в топ N: ")

    get_top_vacancies(top_n, list_object_filter)


user()
