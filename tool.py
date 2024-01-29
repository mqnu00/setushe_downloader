import requests
from urllib import parse
import pickle
import os
import json

import base_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Referer': 'https://setushe.com/',
}


def get_html_content(url):
    cnt = 100
    while cnt > 0:
        try:
            response = requests.get(
                url=url,
                headers=headers
            )
            if response.status_code != 200:
                cnt = cnt - 1
                continue
            return response.content
        except Exception as e:
            print(e)
            cnt = cnt - 1
    return False


def get_url_parser(url):
    res = parse.urlparse(url)
    return res


def path_exist(path):
    return os.path.exists(path)


def create_folder(path):
    if path_exist(path):
        return
    os.mkdir(path)


def path_merge(li):
    path = ''
    for i in li:
        path = os.path.join(path, i)
    return path


def get_list(path, name):
    create_folder(path)
    now = path_merge([path, name])
    with open(now, 'rb') as f:
        data = pickle.load(f)
    return data


def save_list(path, name, data):
    create_folder(path)
    now = path_merge([path, name])
    with open(now, 'wb') as f:
        pickle.dump(data, f)


def save_json(path, name, data):
    create_folder(path)
    now = path_merge([path, name])
    with open(now, 'w', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False)
        f.write(data)


def get_json(path, name):
    create_folder(path)
    now = path_merge([path, name])
    with open(now, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def write_file(path, name, data):
    create_folder(path)
    now = path_merge([path, name])
    with open(now, 'wb') as f:
        f.write(data)


def get_path_and_name(folder_path):
    files = os.listdir(folder_path)
    res = list()
    for file in files:
        path = path_merge([folder_path, file])
        if os.path.isfile(path):
            continue
        data = dict()
        data['folder_path'] = path
        tmp = os.listdir(path)
        for i in tmp:
            i = str(i)
            if i.find('json') != -1:
                data['json_name'] = i
                break
        res.append(data)
    return res


if __name__ == '__main__':
    print(get_path_and_name(base_data.path))
    pass
