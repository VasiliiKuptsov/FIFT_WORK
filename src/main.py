import requests
import os
import psycopg2
from run import get_company, get_vacancy
from dbmanager import DBManager

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН  """

def main():
    dbmanager = DBManager('postgres', 'postgres', '1705', 'localhost', '5432')

    #cursor = connection.cursor()
    #sql = "CREATE DATABASE hh"
    #cursor.execute(sql)
    #cursor.commit()
    dbmanager.create_database('hh')
    dbmanager = DBManager('hh', 'postgres', '1705', 'localhost', '5432')
    dbmanager.create_table()
    #conn.autocommit = True
    data = [5155512, 4971283, 5214704, 93051, 5060211, 2393, 6164545, 2650528, 1684993, 6093775]
    for dat in data:
        print(get_company(dat))
        company = get_company(dat)
        vacancies = get_vacancy(dat)
        i = 0
        for vacancy in vacancies:
            dbmanager.insert_values_vacancies(vacancy)
            i+=1
            print(vacancy)
        print(i)
        #dbmanager.close_conn()
        #close_conn()
        dbmanager.insert_values_employee(company)


        #dbmanager.insert_values_vacancies(vacancies)
    dbmanager.close_conn()
    breake



main()