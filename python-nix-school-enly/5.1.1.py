import json
import requests


# task_1
def parse_site():
    test_payload = 'https://nghttp2.org/httpbin'
    r = requests.get(url=f'{test_payload}/spec.json',
                     headers={'user-agent': 'Python Learning Requests'})
    paths_dict = json.loads(r.text)['paths']
    not_200_dict = {}
    for url in paths_dict:
        for method in paths_dict[url]:
            for response in paths_dict[url][method]['responses']:
                if response != '200':
                    not_200_dict[f'{test_payload}{url}'] = response

    return f'\n task_1 {not_200_dict}'


# task_2
def submit_order(submit_headers, submit_data):
    r = requests.post(url='http://httpbin.org/post', headers=submit_headers, data=submit_data)
    response = json.loads(r.text)['form']
    return f'\n task_2 {response, r.headers}'


# task_3_1/3_2  https://restcountries.eu/rest/v1/all не работает, a http://api.countrylayer.com/v2/all
# не возвращает 'languages', поэтому задание 3 не может быть выполнено
def find_countries():
    r = requests.get(url='http://api.countrylayer.com/v2/all',
                     params={'access_key': 'e11a4ba552717b1d0636fa62b3c37180'},
                     headers={'User-Agent': 'Python Learning Requests'})
    return f'\n task_3 can not be done completed, see comments {json.loads(r.text)}'


if __name__ == "__main__":
    print(parse_site())
    print(submit_order(submit_headers={'user-agent': 'Python Learning Requests'},
                       submit_data={'custname': 'Ень Лидия', 'custtel': '+3323233232%%%', 'custemail': 'lidiya@gmail.com',
                                    'size': 'medium', 'topping': ['bacon', 'cheese', 'mushroom'], 'delivery': '20:00',
                                    'comments': 'Науки, 2a/18'}
                       )
          )
    print(find_countries())
