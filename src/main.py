import requests
import os
from run import get_company, get_vacancy

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН  """

def main():
    data = [5155512, 4971283, 5214704, 93051, 5060211, 2393, 6164545, 2650528, 1684993, 6093775]
    for dat in data:
        #print(get_company(dat))#keyword = input(' ВВЕДИТЕ КЛЮЧЕВОЕ СЛОВО   ')
        print(get_vacancy(dat))
    breake

    page = 0
    hh_pages = 1
    hh_close = False


    while not hh_close:
        if page < hh_pages:
            hh_run.params['page'] = page
            page += 1
            hh_emplouers = hh_run.get_request().json()
            print(hh_emplouers)
            #hh_pages = hh_emplouers['page']
            #hh_items = hh_vacancies['items']

        else:
            hh_close = True


main()