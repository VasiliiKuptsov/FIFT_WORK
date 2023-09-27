import requests
import os




def get_company(company_id):

    headers = {'User-Agent':'HH-User_Agent'}
    url = f'https://api.hh.ru/employers/{company_id}'
    response = requests.get(url, headers=headers)
    response = response.json()
    data = {'hh_id': response.get('id'),
            'name': response.get('name'),
            'description': response.get('description'),
            'url_company': response.get('alternate_url'),
            'area': response.get('area')['name']
    }
    return data

def get_vacancy(company_id):
    vacancies = []
    headers = {'User-Agent': 'HH-User_Agent'}
    url = f'https://api.hh.ru/vacancies?employer_id={company_id}'
    response = requests.get(url, headers=headers)
    response = response.json()
    for vacancy in response.get('items'):
        vacancies.append({'hh_id':vacancy.get('id'),
        'name': vacancy.get('name'),
        'salary_from': vacancy.get('salary')['from']if vacancy.get('salary') else None,
        'salary_to': vacancy.get('salary')['to']if vacancy.get('salary')  else None,
        'salary_to': vacancy.get('salary')['currency']if vacancy.get('salary') else None,
        'requirements': vacancy.get('snippet')['requirement']
        }
                         )
    return vacancies