from src.file_seve import Json
from src.job_processing import One_Vacancy


def test_file_save():

    json_file = Json("opa")
    vakansii = One_Vacancy(
        "Тестировщик комфорта квартир",
        350000,
        "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    )
    vakansi2 = One_Vacancy(
        "Тестировщик комфорта",
        350000,
        "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    )
    json_file.json_save([vakansii, vakansi2])
    list123 = vakansii.vacancy_dict
    list123.extend(vakansi2.vacancy_dict)
    list_json = json_file.json_give()
    assert list_json == list123
    vakansi3 = One_Vacancy(
        "Тестировщик комфорта",
        350000,
        "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    )
    vakansi4 = One_Vacancy(
        "Тестировщик",
        350000,
        "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    )
    json_file.json_save([vakansi3, vakansi4])
    list_json = json_file.json_give()
    list123.extend(vakansi4.vacancy_dict)
    assert list_json == list123
    json_file.json_delite("Тестировщик")
    list_json = json_file.json_give()
    list123.pop(2)
    assert list_json == list123
