import json
import requests
import pytest

# pytest -v  python-nix-school-enly/test_6_3_1.py --rounding_index 7
# pytest -v  python-nix-school-enly/test_6_3_1.py -m add


url = 'http://api.mathjs.org/v4/'
headers = {'User-Agent': 'Python Learning Requests', 'content-type': 'application/json'}


@pytest.mark.add
@pytest.mark.parametrize('a', [5, -1])
@pytest.mark.parametrize('b', [0, -2])
def test_add(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}+{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a + b


@pytest.mark.add
@pytest.mark.xfail
@pytest.mark.parametrize('a', ['n'])
@pytest.mark.parametrize('b', [-1])
def test_add_negative(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}+{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a + b


@pytest.mark.subtract
@pytest.mark.parametrize('a', [5, -1])
@pytest.mark.parametrize('b', [0, -2])
def test_subtract(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}-{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a - b


@pytest.mark.subtract
@pytest.mark.xfail
@pytest.mark.parametrize('a', [3])
@pytest.mark.parametrize('b', [True])
def test_subtract_negative(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}-{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a - b


@pytest.mark.multiply
@pytest.mark.parametrize('a', [5, -1])
@pytest.mark.parametrize('b', [0, 2, -2])
def test_multiply(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}*{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a * b


@pytest.mark.multiply
@pytest.mark.xfail
@pytest.mark.parametrize('a', [3])
@pytest.mark.parametrize('b', ['n'])
def test_multiply_negative(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}*{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a * b


@pytest.mark.divide
@pytest.mark.parametrize('a', [6, -1])
@pytest.mark.parametrize('b', [2, -4])
def test_divide(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}/{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a / b


@pytest.mark.divide
@pytest.mark.xfail
@pytest.mark.parametrize('a', [3])
@pytest.mark.parametrize('b', [0, 'n'])
def test_divide_negative(a, b, get_rounding_index):
    data = json.dumps({'expr': '{0}/{1}'.format(a, b), 'precision': get_rounding_index})
    r = requests.post(url, data=data, headers=headers)
    response = json.loads(r.text)['result']
    assert float(response) == a / b


@pytest.mark.square_root
@pytest.mark.parametrize('a', [3, 0])
def test_square_root(a, get_rounding_index):
    r = requests.get(url + '?expr=sqrt({})&precision={}'.format(a, get_rounding_index), headers=headers)
    response = r.json()
    assert float(response) == a ** (1 / 2)


@pytest.mark.square_root
@pytest.mark.xfail
@pytest.mark.parametrize('a', [-9])
def test_square_root_negative(a, get_rounding_index):
    r = requests.get(url + '?expr=sqrt({})&precision={}'.format(a, get_rounding_index), headers=headers)
    response = r.json()
    assert float(response) == a ** (1 / 2)
