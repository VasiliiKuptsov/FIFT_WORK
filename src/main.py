
from run import get_company, get_vacancy
from dbmanager import DBManager

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН  """

def main():
    dbmanager = DBManager('postgres', 'postgres', '1705', 'localhost', '5432')
    dbmanager.create_database('hh')
    dbmanager = DBManager('hh', 'postgres', '1705', 'localhost', '5432')
    dbmanager.create_table()
    #conn.autocommit = True
    data = [5155512, 4971283, 5214704, 93051, 5060211, 2393, 6164545, 2650528, 1684993, 6093775]
    number_id = []
    count = 0
    for dat in data:
        #print(get_company(dat))
        company = get_company(dat)
        vacancies = get_vacancy(dat)
        i = 0
        for vacancy in vacancies:
            dbmanager.insert_values_vacancies(vacancy,dat)
            i+=1
            #print(vacancy)
        number_id.append(i)
        dbmanager.insert_values_employee(company,number_id[count])
        count +=1
    dbmanager.get_companies_and_vacancies_count(company,number_id)
    dbmanager.get_all_vacancies()
    dbmanager.get_avg_salary()
    dbmanager.get_vacancies_with_higher_salary()
    dbmanager.get_vacancies_with_keyword()
    dbmanager.close_conn()
    breake



main()