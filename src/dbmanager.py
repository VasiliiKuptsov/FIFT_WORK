import requests
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
        self.cursor.execute('''CREATE TABLE employee(hh_id int,
                                                          name varchar(40),
                                                          description text,
                                                          url_company varchar(30),
                                                          area varchar(20))''');
        self.cursor.execute('''CREATE TABLE vacancies( hh_id varchar(20),
                                                       name text,
                                                       salary_from varchar(20),
                                                       salary_to varchar(20),
                                                       requirements text
                                                       )''');



    def insert_values_employee(self, dat):
         self.cursor = self.conn.cursor()
         self.cursor.execute('''
                        INSERT INTO employee(hh_id, name, description, url_company, area)
                        VALUES( %s, %s, %s, %s, %s)''',
                        (dat['hh_id'], dat['name'], dat['description'], dat['url_company'], dat['area'])
                        )


    def insert_values_vacancies(self, dat):
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                               INSERT INTO vacancies(hh_id, name, salary_from, salary_to, requirements)
                               VALUES( %s, %s, %s, %s, %s)''',
                            (dat['hh_id'], dat['name'], dat['salary_from'], dat['salary_to'], dat['requirements'])
                            )






#self.cursor.commit()

"""

получает список всех компаний и количество вакансий у каждой компании.

    def get_companies_and_vacancies_count():

        pass

         получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    def get_all_vacancies():
        pass
        получает среднюю зарплату по вакансия
    def  get_avg_salary():
        pass
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    def get_vacancies_with_higher_salary():
        pass


    def  get_vacancies_with_keyword():
        pass """

