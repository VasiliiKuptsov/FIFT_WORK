class DBManager:



    def __init__(self, db_user, db_password, db_host, db_port):

        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port)
        self.connection = psycopg2.connect(db_name = 'postgres',
                                            user = self.db_user,
                                            password = self.db_password,
                                            host = self.db_host,
                                            port = self.db_port)


    def create_database(self, db_name):
        self.cursor = self.connection.cursor()
        self.cursor.execute('DROP DATABASE IF EXISTS {db_name}')
        self.cursor.execute('CREATE DATABASE {db_name}')
        self.cursor.commit()


    def create_table(self):


        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE employee ...;')
        self.cursor.execute('CREATE TABLE vacancies ...;')
        self.cursor.commit()



    """получает список всех компаний и количество вакансий у каждой компании. """

    def get_companies_and_vacancies_count():

    """ получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
    def get_all_vacancies():

    """ получает среднюю зарплату по вакансиям"""
    def  get_avg_salary():

    """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
    def get_vacancies_with_higher_salary():

    """ получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
    def  get_vacancies_with_keyword():


    def close_connection(self):