import json
import requests


def parse_site():
    test_payload = 'https://nghttp2.org/httpbin'
    r = requests.get(url=f'{test_payload}/spec.json',
                     headers={'user-agent': 'Python Learning Requests'})
    paths_dict = json.loads(r.text)['paths']
    no_200_dict = {}
    for url in paths_dict:
        for method in paths_dict[url]:
            for response in paths_dict[url][method]['responses']:
                if response != '200':
                    no_200_dict[f'{test_payload}{url}'] = response

    return no_200_dict


if __name__ == "__main__":
    print(parse_site())

