import json
import requests


# task_1
def get_not200():
    test_payload = 'https://nghttp2.org/httpbin'
    r = requests.get(url=f'{test_payload}/spec.json',
                     headers={'User-Agent': 'Python Learning Requests'})
    paths_dict = json.loads(r.text)['paths']
    not_200_dict = {}
    for url in paths_dict:
        for method in paths_dict[url]:
            for response in paths_dict[url][method]['responses']:
                if response != '200':
                    not_200_dict[f'{test_payload}{url}'] = response

    return not_200_dict


# task_2
def submit_order():
    submit_headers = {'User-Agent': 'Python Learning Requests'}
    submit_data = {'custname': 'Ень Лидия', 'custtel': '+3323233232%%%', 'custemail': 'lidiya@gmail.com',
                   'size': 'medium', 'topping': ['bacon', 'cheese', 'mushroom'],
                   'delivery': '20:00', 'comments': 'Науки, 2a/18'}
    r = requests.post(url='http://httpbin.org/post', headers=submit_headers, data=submit_data)
    response = json.loads(r.text)['form']
    return response, r.headers


# task_3_1  API https://restcountries.com/v3.1/all
def get_all_languages():
    response_json = requests.get(url='https://restcountries.com/v3.1/all',
                                 headers={'User-Agent': 'Python Learning Requests'}).json()
    languages = set()
    for a in range(0, len(response_json)):
        try:
            for country in response_json:
                languages.update(country['languages'])
        except KeyError:
            pass
    return sorted(languages)


# task 3_2 API https://restcountries.com/v3.1/all
def get_lang_population(lang_codes: list):
    response_json = requests.get(url='https://restcountries.com/v3.1/all',
                                 headers={'User-Agent': 'Python Learning Requests'}).json()
    population = {}
    for a in range(0, len(response_json)):
        try:
            for lang in response_json[a].get('languages'):
                if lang in lang_codes:
                    try:
                        population[lang] += response_json[a]['population']
                    except KeyError:
                        population[lang] = response_json[a]['population']
        except TypeError:
            pass

    return population


if __name__ == "__main__":
    lang_codes_list = ['eng', 'rus', 'fra', 'spa', 'zho']
    #print(f'\n task_1 {get_not200()}')
    #print(f'\n task_2 {submit_order()}')
    print(f'\n task_3.1 {get_all_languages()}')
    print(f'\n task_3.2 {get_lang_population(lang_codes_list)}')

