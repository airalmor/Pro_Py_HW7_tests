import yadisk
import requests

TOKEN_YD = ' Ваш токен яндекса'

def make_dir(dir_name: str):
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN_YD}'
    }
    params = {'path': dir_name}
    response = requests.put(files_url, headers=headers, params=params)
    return response

make_dir('test_make_dir')