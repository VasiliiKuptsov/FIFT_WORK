import requests

url = "https://api.hh.ru/vacancies/"
params = {"text":"python", "page": 1, "per_page":50,"search_field": 'name'}
request = requests.get(url, params = params)
request = request.json()
data = {}
i=0
#for request_ in request:
#print(data)
print(request)

das = {'gas':'daf', 'has':{'jas':'kas', 'las':'pas'}}
print (das['has']['las'])