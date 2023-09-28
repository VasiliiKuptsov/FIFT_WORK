
import psycopg2
class DBManager:


    def __init__(self,db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.conn = psycopg2.connect( dbname = self.db_name,
                                            user = self.db_user,
                                            password = self.db_password,
                                            host = self.db_host,
                                            port = self.db_port

                                      )
        self.conn.autocommit = True

    def close_conn(self):
        self.conn.close()



    def create_database(self, db_name):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''DROP DATABASE IF EXISTS hh;''');
        sql = 'CREATE DATABASE hh'
        self.cursor.execute(sql)




    def create_table(self):

        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE employee( hh_id_company int,
                                                      name varchar(40),
                                                      url_company varchar(30),
                                                      area text,
                                                      description text,
                                                      count_vacancy int) ''');
        self.cursor.execute('''CREATE TABLE vacancies(hh_id_company int,
                                                       hh_id varchar(20),
                                                       url_vacancy varchar(60),
                                                       name text,
                                                       salary_from int,
                                                       salary_to varchar(20),
                                                       requirements text
                                                       )''');



    def insert_values_employee(self, dat, count_vacancy):
         self.cursor = self.conn.cursor()
         self.cursor.execute('''
                        INSERT INTO employee(hh_id_company, name, url_company, area, description, count_vacancy)
                        VALUES( %s, %s, %s, %s, %s, %s)''',
                        (dat['hh_id_company'], dat['name'], dat['url_company'], dat['area'], dat['description'], count_vacancy )
                        )


    def insert_values_vacancies(self, dat, hh_id_company):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                               INSERT INTO vacancies(hh_id_company, hh_id, url_vacancy, name, salary_from, salary_to, requirements)
                               VALUES( %s, %s, %s, %s, %s, %s, %s)''',
                               (hh_id_company, dat['hh_id'], dat['url_vacancy'], dat['name'], dat['salary_from'], dat['salary_to'], dat['requirements'])
                               )


#self.cursor.commit(
    '''получает список всех компаний и количество вакансий у каждой компании.'''

    def get_companies_and_vacancies_count(self, data, number_id ):

        self.cursor = self.conn.cursor()
        self.cursor.execute(f'''SELECT name, count_vacancy from employee''');




    #'''    получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    def get_all_vacancies(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(''' SELECT vacancies.name, employee.name, vacancies.salary_from, 
                                vacancies.url_vacancy from employee
                                inner join vacancies using(hh_id_company)
                             ''');
        
        
    ''' получает среднюю зарплату по вакансия'''
    def  get_avg_salary(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT AVG(salary_from) FROM vacancies; ''')



    '''получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.'''
    def get_vacancies_with_higher_salary(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT * FROM vacancies
                            WHERE salary_from > (SELECT AVG(salary_from)
                            FROM vacancies); ''')


    '''получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.'''
    def  get_vacancies_with_keyword(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT * FROm vacancies WHERE name LIKE '%Python%'; ''')


