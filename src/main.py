import requests
import os
import psycopg2
from run import get_company, get_vacancy
from dbmanager import DBManager

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН  """

def main():
    dbmanager = DBManager('app', '123qwe', '127.0.0.1', '5433')
    dbmanager.create_database('hh')
    dbmanager.create_table()
    data = [5155512, 4971283, 5214704, 93051, 5060211, 2393, 6164545, 2650528, 1684993, 6093775]
    for dat in data:
        #print(get_company(dat))


        #print(get_vacancy(dat))
        dbmanager.insert_values('employee', get_company)
        #dbmanager.insert_values('vacancies', get_vacancy)
    breake



main()